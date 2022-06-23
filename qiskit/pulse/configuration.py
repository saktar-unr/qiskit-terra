# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Configurations for pulse experiments.
"""
from typing import Dict, Union, Tuple, Optional

from .channels import PulseChannel, DriveChannel, MeasureChannel
from .exceptions import PulseError


class Kernel:
    """Settings for this Kernel, which is responsible for integrating time series (raw) data
    into IQ points.
    """

    def __init__(self, name: Optional[str] = None, **params):
        """Create new kernel.

        Args:
            name: Name of kernel to be used
            params: Any settings for kerneling.
        """
        self.name = name
        self.params = params

    def __repr__(self):
        return "{}({}{})".format(
            self.__class__.__name__,
            "'" + self.name + "', " or "",
            ", ".join(f"{str(k)}={str(v)}" for k, v in self.params.items()),
        )


class Discriminator:
    """Setting for this Discriminator, which is responsible for classifying kerneled IQ points
    into 0/1 state results.
    """

    def __init__(self, name: Optional[str] = None, **params):
        """Create new discriminator.

        Args:
            name: Name of discriminator to be used
            params: Any settings for discrimination.
        """
        self.name = name
        self.params = params

    def __repr__(self):
        return "{}({}{})".format(
            self.__class__.__name__,
            "'" + self.name + "', " or "",
            ", ".join(f"{str(k)}={str(v)}" for k, v in self.params.items()),
        )