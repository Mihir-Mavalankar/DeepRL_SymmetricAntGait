cd ../roboschool
source exports.sh
cd roboschool/cpp-household && make clean && make -j4 && cd ../.. && pip install -e .
cd ../baselines
