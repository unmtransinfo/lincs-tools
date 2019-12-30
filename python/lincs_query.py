#!/usr/bin/env python3
#############################################################################
### LINCS REST API client
### http://lincsportal.ccs.miami.edu/dcic/api/
###
### DEPRECATED API?? See new iLINCS: 
### http://www.ilincs.org/ilincs/APIinfo
### http://www.ilincs.org/ilincs/APIdocumentation
#############################################################################
import sys,os,argparse,re,time,json,logging
#
import rest_utils
#
API_HOST="lincsportal.ccs.miami.edu"
API_BASE_PATH="/dcic/api"
#
#############################################################################
def Autosuggest(base_url, searchTerm, facet, fout):
  tags=None;
  url=base_url+'/autosuggest?searchTerm=%s'%searchTerm
  rval=rest_utils.GetURL(url, parse_json=True)
  logging.info(str(rval))
  return(rval)

#############################################################################
def FetchData(base_url, searchTerm, facet, fout):
  tags=None;
  url=base_url+'/fetchdata?searchTerm=%s'%searchTerm
  rval=rest_utils.GetURL(url, parse_json=True)
  return(rval)

#############################################################################
def FetchEntities(base_url, searchTerm, facet, fout):
  tags=None;
  url=base_url+'/fetchentities?searchTerm=%s'%searchTerm
  rval=rest_utils.GetURL(url, parse_json=True)
  if not rval:
    logging.info('not found: %s'%(searchTerm))
    return(None)
  ent = rval
  if not tags:
    tags = ent.keys()
    fout.write('\t'.join(tags)+'\n')
  vals = [str(ent[tag]) if tag in ent else '') for tag in tags]
  fout.write('\t'.join(vals)+'\n')

#############################################################################
if __name__=='__main__':
  epilog='''\
API_HOST: %(API_HOST)s
'''%{'API_HOST':API_HOST}
  parser = argparse.ArgumentParser(description='LINCS Portal REST API client utility', epilog=epilog)
  ops = ['fetchEntities', 'fetchData', 'autoSuggest']
  parser.add_argument("op", choices=ops, help='operation')
  parser.add_argument("--searchTerm", dest="searchTerm", help="Entity searchTerm e.g. Rock1)")
  parser.add_argument("--i", dest="ifile", help="input file, PubMed IDs")
  parser.add_argument("--facet", dest="facet", help="search facet")
  parser.add_argument("--nmax", type=int, help="max results")
  parser.add_argument("--skip", type=int, help="skip results")
  parser.add_argument("--o", dest="ofile", help="output (CSV)")
  parser.add_argument("--api_host", default=API_HOST)
  parser.add_argument("--api_base_path", default=API_BASE_PATH)
  parser.add_argument("-v", "--verbose", action="count", default=0)

  args = parser.parse_args()

  BASE_URL='http://'+args.api_host+args.api_base_path

  if args.ofile:
    fout=open(args.ofile,"w+")
    if not fout: parser.error('cannot open outfile: %s'%args.ofile)
  else:
    fout=sys.stdout

  if args.op == 'fetchEntities':
    if not args.searchTerm:
      parser.error('Requires searchTerm.')
    FetchEntities(BASE_URL, args.searchTerm, args.facet, fout)

  elif args.op == 'fetchData':
    if not args.searchTerm:
      parser.error('Requires searchTerm.')
    FetchData(BASE_URL, args.searchTerm, args.facet, fout)

  elif args.op == 'autoSuggest':
    if not args.searchTerm:
      parser.error('Requires searchTerm.')
    Autosuggest(BASE_URL, args.searchTerm, args.facet, fout)

  else:
    parser.error('No operation specified.')
    parser.print_help()

