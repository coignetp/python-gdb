#include <iostream>

int fib(int n) {
  if (n < 0)
    throw std::invalid_argument("Invalid fibonacci argument");
  
  if (n == 0 || n == 1)
    return 1;

  return fib(n-1) + fib(n-2);
}

int main(int argc, char **argv) {
  if (argc < 2)
    std::invalid_argument("Usage like : ./fib <n>");

  int n = std::stoi(argv[1]);
  std::cout << "Fib " << n << ": " << fib(n) << std::endl;

  return 0;
}