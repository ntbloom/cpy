#include "number.h"
#include <iostream>
#include <yaml-cpp/yaml.h>

using std::cout;
using std::endl;

int Number::answer() {
  YAML::Emitter out{};
  out << "confirmation that we can use yaml-cpp";
  cout << out.c_str() << endl;
  return 42;
}
