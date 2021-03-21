import argparse

my_parser = argparse.ArgumentParser(allow_abbrev=False)
subparser = my_parser.add_subparsers()
sort_parser = subparser.add_parser('sort', help='Sort files in a directory')
sort_parser.add_argument('dir_path',action='store')
sort_parser.add_argument('sort_by',action='store',choices=['size','ext'])
sort_parser.set_defaults(which='sort')


merge_parser = subparser.add_parser('merge_pdf', help='Merge different PDFs into a single PDF')
merge_parser.add_argument('pdf_list',action='store',nargs='+')
merge_parser.add_argument('out_path',action='store')
merge_parser.set_defaults(which='merge_pdf')

resize_parser = subparser.add_parser('resize_image', help='Resize an input image')
resize_parser.add_argument('--h',action='store',type=int)
resize_parser.add_argument('--w',action='store',type=int)
resize_parser.add_argument('image_path',action='store')
resize_parser.add_argument('out_path',action='store')
resize_parser.set_defaults(which='resize_image')

filter_parser = subparser.add_parser('filter_image', help='Apply various filters to an input image')
filter_parser.add_argument('image_path',action='store')
filter_parser.add_argument('filter_name',action='store',choices=['f1','f2'])
filter_parser.add_argument('out_path',action='store')
filter_parser.set_defaults(which='filter_image')

download_parser = subparser.add_parser('download_image', help='Download an image')
download_parser.add_argument('image_path',action='store')
download_parser.add_argument('out_path',action='store')
download_parser.set_defaults(which='download_image')

pdf_crop_parser = subparser.add_parser('crop_pdf', help='Resize an input image')
pdf_crop_parser.add_argument('--s',action='store',type=int)
pdf_crop_parser.add_argument('--e',action='store',type=int)
pdf_crop_parser.add_argument('pdf_path',action='store')
pdf_crop_parser.add_argument('out_path',action='store')
pdf_crop_parser.set_defaults(which='crop_pdf')

args = my_parser.parse_args()

if args.which=='sort':
    from files_package import file_utility
    file_utility.sort_files(args.dir_path,args.sort_by)
elif args.which=='merge_pdf':
    from pdf_package import pdf_utility
    pdf_utility.PDF_merger(args.pdf_list,args.out_path)
elif args.which=='crop_pdf':
    from pdf_package import pdf_utility
    pdf_utility.PDF_croper(args.pdf_path,args.s,args.e,args.out_path)


