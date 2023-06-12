#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - prints information about a python object
 * @p: the python object to print its information
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	PyObject *l;
	PyListObject *ll;
	int i;

	l = (PyObject *)p;
	ll = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", PyList_Size(l));
	printf("[*] Allocated = %ld\n", ll->allocated);
	for (i = 0; i < PyList_Size(l); i++)
	{
		printf("Element %d: %s\n", i, ll->ob_item[i]->ob_type->tp_name);
	}
}
