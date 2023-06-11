#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - prints information about a python object
 * @p: the python object to print its information
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	PyListObject * l;

	l = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld", PyList_Size(p));
}
