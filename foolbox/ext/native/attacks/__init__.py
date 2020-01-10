from .basic_iterative_method import L2BasicIterativeAttack  # noqa: F401
from .basic_iterative_method import LinfinityBasicIterativeAttack  # noqa: F401
from .fast_gradient_method import L2FastGradientAttack  # noqa: F401
from .fast_gradient_method import LinfinityFastGradientAttack  # noqa: F401
from .carlini_wagner import L2CarliniWagnerAttack  # noqa: F401
from .ead import EADAttack  # noqa: F401
from .projected_gradient_descent import ProjectedGradientDescentAttack  # noqa: F401
from .contrast import L2ContrastReductionAttack  # noqa: F401
from .contrast import BinarySearchContrastReductionAttack  # noqa: F401
from .contrast import LinearSearchContrastReductionAttack  # noqa: F401
from .inversion import InversionAttack  # noqa: F401
from .blended_noise import LinearSearchBlendedUniformNoiseAttack  # noqa: F401
from .saltandpepper import SaltAndPepperNoiseAttack  # noqa: F401

FGM = L2FastGradientAttack
FGSM = LinfinityFastGradientAttack
PGD = ProjectedGradientDescentAttack