#include <stdio.h>
#include "Python.h"

/**
 * print_python_list - prints some basic information about Python list
 * @p: Python object
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	PyListObject *l;
	int i;

	l = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", l->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", l->allocated);
	for (i = 0; i < l->ob_base.ob_size; i++)
	{
		printf("Element %d: %s\n", i, l->ob_item[i]->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - prints some info about Python bytes
 * @p: Python object
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;

	size = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
		printf("  [ERROR] Invalid Bytes Object\n");
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first %ld bytes: \n", size < 10 ? size : 10);
}
