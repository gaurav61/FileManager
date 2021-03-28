# filezilla, a CLI tool to manage files 

## Prerequisite
* Python>=3.7 and Linux OS.

## Build from the Source Code
* Clone the repository using :-
    ```
    $ git clone https://github.com/gaurav61/FileManager.git
    ```

* Go to the root of the project
	```
    $ cd FileManager
    ```

* Install using
	```
    $ python3 setup.py install
    ```

## Install from PyPI
* Install using
	```
    $ pip install filezilla
    ```

## Usage
### Sort Files
* Sort files in a directory based on the file extension
	```
    $ filezilla sort <ABSOLUTE_PATH_OF_THE_DIRECTORY> ext
    ```

* Sort files in a directory based on the file size
	```
    $ filezilla sort <ABSOLUTE_PATH_OF_THE_DIRECTORY> size
    ```

### Merge PDFs
* Concatenate multiple PDFs into a single PDF
	```
    $ filezilla merge_pdf <ABSOLUTE_PATH_OF_PDF_1> <ABSOLUTE_PATH_OF_PDF_2> ... <ABSOLUTE_PATH_OF_PDF_N> <ABSOLUTE_PATH_OF_OUTPUT_PDF_FILE
    ```