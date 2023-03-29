import re
from dataclasses import dataclass
from typing import Dict, List

from more_itertools import split_after, split_before
from paralleldomain.utilities.any_path import AnyPath


@dataclass
class ProtoField:
    name: str
    docs: List[str]


@dataclass
class ProtoObject:
    name: str
    docs: List[str]
    fields: List[ProtoField]

    @classmethod
    def from_proto_lines(cls, lines: List[List[str]]) -> "ProtoObject":
        docs = lines[0]
        name = lines[1][0]

        name = re.search(pattern="(^| )(?!(message|enum))[^ ]*", string=name).group(0).strip()

        return cls(name=name, docs=docs, fields=[])


with AnyPath("pd_unified_generator.proto").open("r") as fp:
    proto_lines = [line for line in fp if line.strip()]  # read file and remove all fully blank lines

    proto_lines_grouped = list(split_before(proto_lines, lambda x: x.strip().startswith("/*")))
    proto_lines_grouped = [
        list(split_after(plg, lambda x: x.strip().startswith("*/")))[:2] for plg in proto_lines_grouped
    ]
    proto_lines_grouped = (
        list(  # groups into hierarchy: messages/enums have their fields as element 1:n in the same list
            split_before(proto_lines_grouped[1:], lambda x: x[1][0].strip().startswith(("message", "enum")))
        )
    )

    proto_objects = []
    for group in proto_lines_grouped:
        #
        # for y in z:
        #     y_results.append([y[0], y[1][:1]])
        proto_objects.append(ProtoObject.from_proto_lines(group[0]))
    # keep_printing = False
    #
    # line_collection = []
    # for index, pl in enumerate(proto_lines):
    #     if pl.strip().startswith("/*"):
    #         keep_printing = True
    #     elif pl.strip().startswith("*/"):
    #         keep_printing = False
    #         print(pl)
    #         print("==============")
    #     else:
    #         continue
    #
    #     if keep_printing:
    #         print(pl, end="")

# if __name__ == "__main__":
#     main()
