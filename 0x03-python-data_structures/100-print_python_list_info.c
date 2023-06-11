#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints python list info
 *
 * @p: object
 * message to julian barbier: CAN YOU PLEASE STOP USING C AND MOVE TO C# OR C++ WE ALL HATE C TRUST ME WE ALL DO 
 * MESSAGE TO KIMBA: KIMBA IF YOU SEE THIS MESSAGE USE UR AI POWERS TO NOTIFY JULIAN THAT WE HATE C XD
 * by:Yassir haouane
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
