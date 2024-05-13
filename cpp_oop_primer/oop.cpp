#include <iostream>
#include <stdio.h>
#include <string_view>
#include <cassert>

class Date
{
public:
  int day{};
  int month{};
  int year{};
};

void print_string(const char *c) {
  // *c = 'b'; // errors out when const is applied to the param
  while (*c) {
    putchar(*c++);
  }
}

int main()
{
  Date today;
  today.day = 12;
  today.month = 5;
  today.year = 24;

  char str[] = "hello, world!"; // mutable
  // char *str = "hello, world!"; // immutable

  print_string(str);
  return 0;
}


