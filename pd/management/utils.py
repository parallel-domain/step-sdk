# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Utility functions for instance management
"""

import logging
import time
from uuid import UUID


from pd.management.ig import Ig, IgStatus
from pd.core import PdError


logger = logging.getLogger(__name__)


def is_uuid(s: str) -> bool:
    try:
        UUID(s)
    except ValueError:
        return False
    return True


def create_ig_with_retry(max_retries: int = 0, **kwargs) -> Ig:
    """
    Create an IG, retrying if create fails

    Args:
        max_retries: Max retries, 0 for infinite retries
        **kwargs: Kwargs passed to Ig.create()

    Returns:

    """
    max_retries = max(0, max_retries)
    ig = None
    retries = -1  # first create doesn't count towards a retry
    while ig is None or ig.status != IgStatus.Running:
        if ig is None:
            ig = Ig.create(**kwargs)
            retries += 1
            logger.info(f"Ig instance {ig.name} created (retry={retries}/{max_retries})")
        elif ig.status == IgStatus.Stopped:
            if max_retries == 0 or retries < max_retries:
                # Something went wrong starting the instance
                logger.info(f"Ig instance {ig.name} failed to start")
                ig = None
            else:
                # We've exhausted our retries
                raise PdError("Failed to create Ig instance with retries")
        else:
            # Delay before checking again
            time.sleep(5)
            ig = Ig.read(ig.name)

    # Bugfix for Ig networking race condition
    time.sleep(20)

    return ig
