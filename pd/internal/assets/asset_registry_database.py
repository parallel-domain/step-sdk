# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

from peewee import SqliteDatabase, InterfaceError

from pd.core import PdError


class AssetRegistryDatabase(SqliteDatabase):
    def connect(self, *kwargs):
        try:
            super().connect(*kwargs)
        except InterfaceError:
            raise PdError(
                "Couldn't connect to the Asset Registry. "
                "Did you remember to initialize the registry by first calling one of "
                "pd.assets.init_asset_registry_version(...) or "
                "pd.assets.init_asset_registry_file(...) ?"
            )
