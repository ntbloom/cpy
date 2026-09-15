#include <pybind11/pybind11.h>
namespace py = pybind11;

class Number {
public:
  static int answer();
};

PYBIND11_MODULE(cbackend, m, py::mod_gil_not_used()) { // NOLINT
  m.doc() = "pybind example";
  m.def("answer", &Number::answer,
        "answer to the life, the universe, and everything");
}
