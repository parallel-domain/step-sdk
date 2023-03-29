# from pd.internal.proto.keystone.generated.wrapper.utils import AtomicGeneratorMessage
from typing import TypeVar, Union

from google.protobuf.message import Message

PM = TypeVar("PM", bound=Message)


class BaseGenerator:
    ...

    def clone(self):
        raise NotImplementedError()


# AtomicGenerator = Union[BaseGenerator, AtomicGeneratorMessage]
