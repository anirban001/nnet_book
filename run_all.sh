#!/bin/bash
set -e
set -o pipefail

export PROJECT_ROOT=$(git rev-parse --show-toplevel)
export CACHE_DIR="${PROJECT_ROOT}/.cache"

_setup() {
  # # http://docs.python-guide.org/en/latest/dev/virtualenvs/
  # pip install virtualenv
  # brew install wget
  return
  mkdir -p ${CACHE_DIR}
  cd ${CACHE_DIR}
  virtualenv --no-site-packages venv_01
  virtualenv venv_01
  return
}

_activate() {
  cd ${PROJECT_ROOT}
  . ${CACHE_DIR}/venv_01/bin/activate
}

_pip_install() {
  # return
  _activate
  pip install $1
  pip freeze > ./requirements.txt
  # return
  # Re-install.
  # _activate
  # pip install -r ./requirements.txt
}

_run_it() {
  _activate
  time python2.7 -c 'import code_dir.main; code_dir.main.do_main()'
}

cd ${PROJECT_ROOT}
# (_setup)
# (_pip_install numpy)
# (_pip_install scipy)
# (_pip_install scikit-learn)
(_run_it)

echo 'Done'
