from datetime import datetime, timezone, timedelta

import pytest
import requests_mock

import pd.management
from pd.management import Ig, IgVersion, IgStatus, Levelpak, LevelpakVersion, IgQuality, SimVersion, LabelEngineVersion

_BASE_URL = pd.management.api_url


@pytest.fixture(autouse=True)
def setup_management():
    pd.management.org = 'test'
    pd.management.api_key = 'testapikey'


class TestIg:
    @requests_mock.Mocker(kw='m')
    def test_create(self, **kwargs):
        """Correctly calls API to create Ig object"""
        m = kwargs['m']
        m.post(f'{_BASE_URL}/test/ig', json={
            'ig_version': 'v1.2.3',
            'self_url': 'https://domain/org/ig/abc123',
            'status': 'starting',
            'ig_url': None,
            'created_at': '2022-04-08T07:36:04+05:00',
            'levelpak': {}
        })
        ig = Ig.create(levelpaks={})
        assert m.last_request
        data = m.last_request.json()
        assert data['levelpak'] == {}
        assert ig
        assert ig.ig_version == 'v1.2.3'
        assert ig.self_url == 'https://domain/org/ig/abc123'
        assert ig.status == IgStatus.Starting
        assert ig.ig_url is None
        assert ig.created_at == datetime(2022, 4, 8, 7, 36, 4, tzinfo=timezone(timedelta(seconds=18000)))
        assert ig.levelpak == {}

    @requests_mock.Mocker(kw='m')
    def test_create_with_ig_version(self, **kwargs):
        """Correctly calls API to create Ig object with ig_version"""
        m = kwargs['m']
        m.post(f'{_BASE_URL}/test/ig', json={
            'ig_version': 'my-custom-version',
            'self_url': 'https://domain/org/ig/abc123',
            'status': 'starting',
            'ig_url': None,
            'created_at': '2022-04-08T07:36:04+05:00',
            'levelpak': {}
        })
        ig = Ig.create(ig_version='my-custom-version')
        assert m.last_request
        data = m.last_request.json()
        assert data['ig_version'] == 'my-custom-version'
        assert ig

    @requests_mock.Mocker(kw='m')
    def test_create_with_sim_version(self, **kwargs):
        """Correctly calls API to create Ig object with sim_version"""
        m = kwargs['m']
        m.post(f'{_BASE_URL}/test/ig', json={
            'sim_version': 'my-sim-version',
            'ig_version': '',
            'self_url': 'https://domain/org/ig/abc123',
            'status': 'starting',
            'ig_url': None,
            'created_at': '2022-04-08T07:36:04+05:00',
            'levelpak': {}
        })
        ig = Ig.create(sim_version='my-sim-version')
        assert m.last_request
        data = m.last_request.json()
        assert data['sim_version'] == 'my-sim-version'
        assert ig

    @requests_mock.Mocker(kw='m')
    def test_create_with_le_version(self, **kwargs):
        """Correctly calls API to create Ig object with le_version"""
        m = kwargs['m']
        m.post(f'{_BASE_URL}/test/ig', json={
            'sim_version': '',
            'ig_version': '',
            'le_version': 'my-le-version',
            'self_url': 'https://domain/org/ig/abc123',
            'status': 'starting',
            'ig_url': None,
            'created_at': '2022-04-08T07:36:04+05:00',
            'levelpak': {}
        })
        ig = Ig.create(le_version='my-le-version')
        assert m.last_request
        data = m.last_request.json()
        assert data['le_version'] == 'my-le-version'
        assert ig

    @requests_mock.Mocker(kw='m')
    def test_create_with_quality(self, **kwargs):
        """Correctly calls API to create Ig object with quality"""
        m = kwargs['m']
        m.post(f'{_BASE_URL}/test/ig', json={
            'ig_version': '',
            'self_url': 'https://domain/org/ig/abc123',
            'status': 'starting',
            'ig_url': None,
            'created_at': '2022-04-08T07:36:04+05:00',
            'levelpak': {}
        })
        ig = Ig.create(quality=IgQuality.High)
        assert m.last_request
        data = m.last_request.json()
        assert data['quality'] == 'high'
        assert ig

    @requests_mock.Mocker(kw='m')
    def test_create_with_default_quality(self, **kwargs):
        """Correctly calls API to create Ig object with default quality"""
        m = kwargs['m']
        m.post(f'{_BASE_URL}/test/ig', json={
            'ig_version': '',
            'self_url': 'https://domain/org/ig/abc123',
            'status': 'starting',
            'ig_url': None,
            'created_at': '2022-04-08T07:36:04+05:00',
            'levelpak': {}
        })
        ig = Ig.create()
        assert m.last_request
        data = m.last_request.json()
        assert data['quality'] == 'high'
        assert ig

    @requests_mock.Mocker(kw='m')
    def test_create_with_levelpaks(self, **kwargs):
        """Correctly calls API to create Ig object with levelpaks"""
        m = kwargs['m']
        m.post(f'{_BASE_URL}/test/ig', json={
            'ig_version': '',
            'self_url': 'https://domain/org/ig/abc123',
            'status': 'starting',
            'ig_url': None,
            'created_at': '2022-04-08T07:36:04+05:00',
            'levelpak': {
                'A2_Kerrytown': 'v1',
                'SC_Highlands': 'v3'
            }
        })
        ig = Ig.create(levelpaks={
            "A2_Kerrytown": "v1",
            "SC_Highlands": "v3"
        })
        assert m.last_request
        data = m.last_request.json()
        assert data['levelpak'] == {
            "A2_Kerrytown": "v1",
            "SC_Highlands": "v3"
        }
        assert ig
    @requests_mock.Mocker(kw='m')
    def test_create_with_missing_levelpaks(self, **kwargs):
        """Correctly calls API to create Ig object with no levelpaks"""
        # When no levelpaks are specified, it should send an empty dictionary
        # and not a None
        m = kwargs['m']
        m.post(f'{_BASE_URL}/test/ig', json={
            'ig_version': 'v1.2.3',
            'self_url': 'https://domain/org/ig/abc123',
            'status': 'starting',
            'ig_url': None,
            'created_at': '2022-04-08T07:36:04+05:00',
            'levelpak': {}
        })
        ig = Ig.create()
        assert m.last_request
        data = m.last_request.json()
        assert data['levelpak'] == {}
        assert ig

    @requests_mock.Mocker(kw='m')
    def test_create_with_ttl(self, **kwargs):
        """Correctly calls API to create Ig object with ttl"""
        m = kwargs['m']
        m.post(f'{_BASE_URL}/test/ig', json={
            'ig_version': '',
            'self_url': 'https://domain/org/ig/abc123',
            'status': 'starting',
            'ig_url': None,
            'created_at': '2022-04-08T07:36:04+05:00',
            'levelpak': {}
        })
        ig = Ig.create(ttl=3600)
        assert m.last_request
        data = m.last_request.json()
        assert data['ttl'] == 3600
        assert ig

    @requests_mock.Mocker(kw='m')
    def test_create_with_missing_sim_and_le(self, **kwargs):
        """Correctly calls API with missing Sim and Label Engine support to create Ig"""
        m = kwargs['m']
        m.post(f'{_BASE_URL}/test/ig', json={
            'ig_version': 'test',
            'self_url': 'https://domain/org/ig/abc123',
            'status': 'running',
            'step_url': 'ssl://example.com:3000',
            'created_at': '2022-04-08T07:36:04+05:00',
            'levelpak': {}
        })
        ig = Ig.create(ig_version='test')
        assert m.last_request
        data = m.last_request.json()
        assert data['ig_version'] == 'test'
        assert ig
        assert ig.step_url == 'ssl://example.com:3000'
        assert ig.ig_url == 'ssl://example.com:3000'

    def test_read(self, requests_mock):
        """Correctly calls API to read Ig object"""
        requests_mock.get(f'{_BASE_URL}/test/ig/abc123', json={
            'sim_version': 'v4.5.6',
            'ig_version': 'v1.2.3',
            'le_version': 'v7.8.9',
            'self_url': 'https://domain/org/ig/abc123',
            'status': 'starting',
            'sim_url': None,
            'ig_url': None,
            'le_url': None,
            'created_at': '2022-04-08T07:36:04+05:00',
            'levelpak': {
                'A2_Kerrytown': 'v2.0.0',
                'SF_6thAndMission_medium': 'v1.14.0',
                'SJ_237AndNorth1st': 'v0.0.1'
            }
        })
        ig = Ig.read(name='abc123')
        assert ig
        assert ig.sim_version == 'v4.5.6'
        assert ig.ig_version == 'v1.2.3'
        assert ig.le_version == 'v7.8.9'
        assert ig.self_url == 'https://domain/org/ig/abc123'
        assert ig.status == IgStatus.Starting
        assert ig.sim_url is None
        assert ig.ig_url is None
        assert ig.le_url is None
        assert ig.created_at == datetime(2022, 4, 8, 7, 36, 4, tzinfo=timezone(timedelta(seconds=18000)))
        assert len(ig.levelpak.keys()) == 3
        assert ig.levelpak['A2_Kerrytown'] == 'v2.0.0'
        assert ig.levelpak['SF_6thAndMission_medium'] == 'v1.14.0'
        assert ig.levelpak['SJ_237AndNorth1st'] == 'v0.0.1'

    def test_read_missing_sim_and_le(self, requests_mock):
        """Correctly reads from Ig API with missing Sim and Label Engine support"""
        requests_mock.get(f'{_BASE_URL}/test/ig/abc123', json={
            'ig_version': 'v1.2.3',
            'self_url': 'https://domain/org/ig/abc123',
            'status': 'running',
            'step_url': 'ssl://example.com:3000',
            'created_at': '2022-04-08T07:36:04+05:00',
            'levelpak': {
                'A2_Kerrytown': 'v2.0.0',
                'SF_6thAndMission_medium': 'v1.14.0',
                'SJ_237AndNorth1st': 'v0.0.1'
            }
        })
        ig = Ig.read(name='abc123')
        assert ig
        assert ig.sim_version is None
        assert ig.ig_version == 'v1.2.3'
        assert ig.self_url == 'https://domain/org/ig/abc123'
        assert ig.status == IgStatus.Running
        assert ig.sim_url is None
        assert ig.step_url == 'ssl://example.com:3000'
        assert ig.ig_url == 'ssl://example.com:3000'
        assert ig.created_at == datetime(2022, 4, 8, 7, 36, 4, tzinfo=timezone(timedelta(seconds=18000)))
        assert len(ig.levelpak.keys()) == 3
        assert ig.levelpak['A2_Kerrytown'] == 'v2.0.0'
        assert ig.levelpak['SF_6thAndMission_medium'] == 'v1.14.0'
        assert ig.levelpak['SJ_237AndNorth1st'] == 'v0.0.1'

    def test_delete(self, requests_mock):
        """Correctly calls API to delete Ig object"""
        requests_mock.delete(f'{_BASE_URL}/test/ig/abc123', text='Deleted')
        Ig.delete(name='abc123')

    def test_list(self, requests_mock):
        """Correctly calls API to list Ig objects"""
        requests_mock.get(f'{_BASE_URL}/test/ig', json={
            'igs': [
                {
                    'sim_version': 'v4.5.6',
                    'ig_version': 'v1.2.3',
                    'le_version': 'v7.8.9',
                    'self_url': 'https://domain/org/ig/abc123',
                    'status': 'starting',
                    'ig_url': None,
                    'le_url': None,
                    'created_at': '2022-04-08T07:36:04+05:00',
                    'shutdown_time': None,
                    'levelpak': {}
                },
                {
                    'sim_version': 'other',
                    'ig_version': 'another',
                    'le_version': 'another2',
                    'self_url': 'https://domain/org/ig/another123',
                    'status': 'running',
                    'sim_url': 'ssl://example.com:3001',
                    'ig_url': 'ssl://example.com:3000',
                    'le_url': 'ssl://example.com:3002',
                    'created_at': '2022-04-08T07:37:04+00:00',
                    'shutdown_time': '2022-04-08T07:42:05+00:00',
                    'levelpak': {}
                },
                {
                    'sim_version': 'latest',
                    'ig_version': 'default',
                    'le_version': 'other',
                    'self_url': 'https://domain/org/ig/default123',
                    'status': 'stopped',
                    'sim_url': None,
                    'ig_url': None,
                    'le_url': None,
                    'created_at': '2022-04-08T08:36:04+01:00',
                    'shutdown_time': None,
                    'levelpak': {}
                },
                {
                    'sim_version': 'v4.5.6',
                    'ig_version': 'v1.2.3',
                    'le_version': 'v7.8.9',
                    'self_url': 'https://domain/org/ig/abc123',
                    'status': 'configuring',
                    'sim_url': None,
                    'ig_url': None,
                    'le_url': None,
                    'created_at': '2022-04-08T07:36:04+05:00',
                    'shutdown_time': None,
                    'levelpak': {
                        'SF_6thAndMission_medium': 'v1'
                    }
                }
            ]
        })
        igs = Ig.list()
        assert igs
        assert len(igs) == 4
        assert igs[0].sim_version == 'v4.5.6'
        assert igs[0].ig_version == 'v1.2.3'
        assert igs[0].le_version == 'v7.8.9'
        assert igs[0].self_url == 'https://domain/org/ig/abc123'
        assert igs[0].status == IgStatus.Starting
        assert igs[0].sim_url is None
        assert igs[0].ig_url is None
        assert igs[0].le_url is None
        assert igs[0].created_at == datetime(2022, 4, 8, 7, 36, 4, tzinfo=timezone(timedelta(seconds=18000)))
        assert igs[0].shutdown_time is None
        assert igs[0].levelpak == {}
        assert igs[1].sim_version == 'other'
        assert igs[1].ig_version == 'another'
        assert igs[1].le_version == 'another2'
        assert igs[1].self_url == 'https://domain/org/ig/another123'
        assert igs[1].status == IgStatus.Running
        assert igs[1].sim_url == 'ssl://example.com:3001'
        assert igs[1].ig_url == 'ssl://example.com:3000'
        assert igs[1].le_url == 'ssl://example.com:3002'
        assert igs[1].created_at == datetime(2022, 4, 8, 7, 37, 4, tzinfo=timezone.utc)
        assert igs[1].shutdown_time == datetime(2022, 4, 8, 7, 42, 5, tzinfo=timezone.utc)
        assert igs[1].levelpak == {}
        assert igs[2].sim_version == 'latest'
        assert igs[2].ig_version == 'default'
        assert igs[2].le_version == 'other'
        assert igs[2].self_url == 'https://domain/org/ig/default123'
        assert igs[2].status == IgStatus.Stopped
        assert igs[2].sim_url is None
        assert igs[2].ig_url is None
        assert igs[2].le_url is None
        assert igs[2].created_at == datetime(2022, 4, 8, 8, 36, 4, tzinfo=timezone(timedelta(seconds=3600)))
        assert igs[2].shutdown_time is None
        assert igs[2].levelpak == {}
        assert igs[3].sim_version == 'v4.5.6'
        assert igs[3].ig_version == 'v1.2.3'
        assert igs[3].le_version == 'v7.8.9'
        assert igs[3].self_url == 'https://domain/org/ig/abc123'
        assert igs[3].status == IgStatus.Configuring
        assert igs[3].sim_url is None
        assert igs[3].ig_url is None
        assert igs[3].le_url is None
        assert igs[3].created_at == datetime(2022, 4, 8, 7, 36, 4, tzinfo=timezone(timedelta(seconds=18000)))
        assert igs[3].shutdown_time is None
        assert igs[3].levelpak == {'SF_6thAndMission_medium': 'v1'}

    def test_list_missing_sim_and_le(self, requests_mock):
        """Correctly calls API to list Ig objects"""
        requests_mock.get(f'{_BASE_URL}/test/ig', json={
            'igs': [
                {
                    'ig_version': 'v1.2.3',
                    'self_url': 'https://domain/org/ig/abc123',
                    'status': 'starting',
                    'step_url': None,
                    'created_at': '2022-04-08T07:36:04+05:00',
                    'shutdown_time': None,
                    'levelpak': {}
                },
                {
                    'ig_version': 'another',
                    'self_url': 'https://domain/org/ig/another123',
                    'status': 'running',
                    'step_url': 'ssl://example.com:3000',
                    'created_at': '2022-04-08T07:37:04+00:00',
                    'shutdown_time': '2022-04-08T07:42:05+00:00',
                    'levelpak': {}
                }
            ]
        })
        igs = Ig.list()
        assert igs
        assert len(igs) == 2
        assert igs[0].sim_version is None
        assert igs[0].ig_version == 'v1.2.3'
        assert igs[0].self_url == 'https://domain/org/ig/abc123'
        assert igs[0].status == IgStatus.Starting
        assert igs[0].sim_url is None
        assert igs[0].ig_url is None
        assert igs[0].step_url is None
        assert igs[0].created_at == datetime(2022, 4, 8, 7, 36, 4, tzinfo=timezone(timedelta(seconds=18000)))
        assert igs[0].shutdown_time is None
        assert igs[0].levelpak == {}
        assert igs[1].sim_version is None
        assert igs[1].ig_version == 'another'
        assert igs[1].self_url == 'https://domain/org/ig/another123'
        assert igs[1].status == IgStatus.Running
        assert igs[1].sim_url is None
        assert igs[1].ig_url == 'ssl://example.com:3000'
        assert igs[1].step_url == 'ssl://example.com:3000'
        assert igs[1].created_at == datetime(2022, 4, 8, 7, 37, 4, tzinfo=timezone.utc)
        assert igs[1].shutdown_time == datetime(2022, 4, 8, 7, 42, 5, tzinfo=timezone.utc)
        assert igs[1].levelpak == {}


class TestIgVersion:
    def test_list(self, requests_mock):
        """Correctly calls API to list IgVersion objects"""
        requests_mock.get(f'{_BASE_URL}/test/ig_versions', json=[
            {
                'name': 'v1.2.3'
            },
            {
                'name': 'another'
            },
            {
                'name': 'default'
            }
        ])
        ig_versions = IgVersion.list()
        assert ig_versions
        assert len(ig_versions) == 3
        assert ig_versions[0].name == 'v1.2.3'
        assert ig_versions[1].name == 'another'
        assert ig_versions[2].name == 'default'


class TestLevelpak:
    def test_list(self, requests_mock):
        """Correctly calls API to list Levelpak objects"""
        requests_mock.get(f'{_BASE_URL}/test/levelpaks', json=[
            {
                'default_version': 'v1',
                'name': 'SC_W8thAndOrchard',
                'versions': [
                    'v1'
                ]
            },
            {
                'default_version': 'v2',
                'name': 'SJ_KettmanAndOrinda_aus',
                'versions': [
                    'v1', 'v2'
                ]
            },
            {
                'default_version': 'v3',
                'name': 'SJ_EssexAndBradford',
                'versions': [
                    'v1', 'v2', 'v3'
                ]
            }
        ])
        levelpaks = Levelpak.list()
        assert levelpaks
        assert len(levelpaks) == 3
        assert levelpaks[0].name == 'SC_W8thAndOrchard'
        assert levelpaks[0].default_version == 'v1'
        assert levelpaks[0].versions == ['v1']
        assert levelpaks[1].name == 'SJ_KettmanAndOrinda_aus'
        assert levelpaks[1].default_version == 'v2'
        assert levelpaks[1].versions == ['v1', 'v2']
        assert levelpaks[2].name == 'SJ_EssexAndBradford'
        assert levelpaks[2].default_version == 'v3'
        assert levelpaks[2].versions == ['v1', 'v2', 'v3']


class TestLevelpakVersions:
    def test_list(self, requests_mock):
        """Correctly calls API to list Levelpak objects"""
        requests_mock.get(f'{_BASE_URL}/test/levelpaks/versions', json=[
            {
                'levelpak': 'SC_W8thAndOrchard',
                'version': 'v1',
                'internal_version': 'uuid_1'
            },
            {
                'levelpak': 'SJ_EssexAndBradford',
                'version': 'v1',
                'internal_version': 'uuid_2'
            },
            {
                'levelpak': 'SJ_EssexAndBradford',
                'version': 'v2',
                'internal_version': 'uuid_3'
            }
        ])
        levelpak_versions = LevelpakVersion.list()
        assert levelpak_versions
        assert len(levelpak_versions) == 3
        assert levelpak_versions[0].levelpak == 'SC_W8thAndOrchard'
        assert levelpak_versions[0].version == 'v1'
        assert levelpak_versions[0].internal_version == 'uuid_1'
        assert levelpak_versions[1].levelpak == 'SJ_EssexAndBradford'
        assert levelpak_versions[1].version == 'v1'
        assert levelpak_versions[1].internal_version == 'uuid_2'
        assert levelpak_versions[2].levelpak == 'SJ_EssexAndBradford'
        assert levelpak_versions[2].version == 'v2'
        assert levelpak_versions[2].internal_version == 'uuid_3'


class TestSimVersion:
    def test_list(self, requests_mock):
        """Correctly calls API to list SimVersion objects"""
        requests_mock.get(f'{_BASE_URL}/test/sim_versions', json=[
            {
                'name': 'v1.2.3'
            },
            {
                'name': 'another'
            },
            {
                'name': 'default'
            }
        ])
        sim_versions = SimVersion.list()
        assert sim_versions
        assert len(sim_versions) == 3
        assert sim_versions[0].name == 'v1.2.3'
        assert sim_versions[1].name == 'another'
        assert sim_versions[2].name == 'default'


class TestLabelEngineVersion:
    def test_list(self, requests_mock):
        """Correctly calls API to list Label Engine objects"""
        requests_mock.get(f'{_BASE_URL}/test/le_versions', json=[
            {
                'name': 'v1.2.3'
            },
            {
                'name': 'another'
            },
            {
                'name': 'default'
            }
        ])
        le_versions = LabelEngineVersion.list()
        assert le_versions
        assert len(le_versions) == 3
        assert le_versions[0].name == 'v1.2.3'
        assert le_versions[1].name == 'another'
        assert le_versions[2].name == 'default'
