from get_hw_spec import *
from get_sw_spec import *

import collections
import oyaml as yaml

def new_empty_section (spec, sec):
  spec[sec] = collections.OrderedDict()
  return spec[sec]

def main():
  specification = collections.OrderedDict()

  current_section = new_empty_section(specification, "hardware")
  current_section["processor"] = get_processor_name()
  current_section["board"] = get_board_name()
  current_section["graphics"] = get_graphics_name()

  current_section = new_empty_section(specification, "software")
  current_section["os"] = get_os_name()
  current_section["kernel"] = get_kernel_release()
  current_section["gcc"] = get_gcc_release()
  current_section["nv_driver"] = get_nv_driver_release()
  current_section["nvcc"] = get_nvcc_release()
  current_section["cuda"] = get_cuda_release()
  current_section["cudnn"] = get_cudnn_release()
  current_section["loaded_so"] = get_loaded_shared_objects()
  current_section["env"] = get_env_variables()
  current_section["python"] = get_python_release()
  current_section["pip"] = get_pip_packages()

  with open('example_current_spec.yml', 'w') as yaml_file:
    yaml.dump(specification, yaml_file, default_style=None, default_flow_style=False)

if __name__ == '__main__':
  main()
