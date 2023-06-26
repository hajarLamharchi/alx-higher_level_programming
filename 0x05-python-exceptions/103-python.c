#include <stdio.h>
#include <stdlib.h>
#include "Python.h"
/**
 * print_python_list - prints basic information about python list
 * @p: python object
 */
void print_python_list(PyObject *p)
{
	PyListObject *l;
	int i;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	l = (PyListObject *)p;
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", l->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", l->allocated);
	for ( i = 0; i < l->ob_base.ob_size; i++)
		printf("Element %d: %s\n", i, l->ob_item[i]->ob_type->tp_name);
}

/**
 * print_python_bytes - prints basic information about python bytes
 * @p: python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;

	size = PyBytes_Size(p);
	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", size);
}

/**
 * print_python_float - prints basic information about python float
 * @p: python object
 */
void print_python_float(PyObject *p)
{
	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	printf("  value: %lf\n", PyFloat_AsDouble(p));
}
