/*
 * Copyright 2017, Adrien Destugues, pulkomandy@pulkomandy.tk
 * Distributed under terms of the MIT license.
 */

#include <private/shared/Json.h>
#include <DataIO.h>

#include <stdio.h>
#include <stdlib.h>


class Fio: public BDataIO
{
	public:
		Fio(FILE* backend)
			: fBackend(backend)
		{
		}

		ssize_t Read(void* buffer, size_t size)
		{
			ssize_t r = fread(buffer, size, 1, fBackend);
			return r;
		}

	private:
		FILE* fBackend;
};


class Listener: public BJsonEventListener
{
	public:
		void Complete()
		{
			fprintf(stderr, "Parsing complete\n");
		}
		void HandleError(long int l, long int c, const char * msg)
		{
			fprintf(stderr, "Error at %ld.%ld: %s\n", l, c, msg);
			exit(EXIT_FAILURE);
		}
		bool Handle(const BPrivate::BJsonEvent & e)
		{
			return true;
		}

};

int main(int argc, char* argv[])
{
	Fio input(stdin);
	Listener listener;
	BJson::Parse(&input, &listener);
	return 0;
}
