import sys
import os

# Hack to enable proto modules to correctly import packages in the same folder
sys.path.append(os.path.dirname(__file__))