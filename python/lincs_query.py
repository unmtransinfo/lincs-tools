#!/usr/bin/env python3
#############################################################################
### LINCS Data Portal  REST API client
###
### http://lincsportal.ccs.miami.edu/dcic/api/fetchentities?searchTerm=Rock1
#############################################################################
import sys,os,argparse,re,time,json,logging
#
import rest_utils
#
API_HOST="lincsportal.ccs.miami.edu"
API_BASE_PATH="/dcic/api"
#
#
#############################################################################
def Autosuggest(base_url, searchTerm, facet, fout, verbose):
  tags=None;
  url=base_url+'/autosuggest?searchTerm=%s'%searchTerm
  rval=rest_utils.GetURL(url, parse_json=True, verbose=verbose)
  logging.info(str(rval))
  return(rval)

#############################################################################
def FetchData(base_url, searchTerm, facet, fout, verbose):
  tags=None;
  url=base_url+'/fetchdata?searchTerm=%s'%searchTerm
  rval=rest_utils.GetURL(url, parse_json=True, verbose=verbose)
  return(rval)

#############################################################################
def FetchEntities(base_url, searchTerm, facet, fout, verbose):
  tags=None;
  url=base_url+'/fetchentities?searchTerm=%s'%searchTerm
  rval=rest_utils.GetURL(url, parse_json=True, verbose=verbose)
  if not rval:
    logging.info('not found: %s'%(searchTerm))
    return(None)
  ent = rval
  if not tags:
    tags = ent.keys()
    fout.write('\t'.join(tags)+'\n')
  vals = [];
  for tag in tags:
    val=(ent[tag] if tag in ent else '')
    vals.append(str(val))
  fout.write('\t'.join(vals)+'\n')

#############################################################################
if __name__=='__main__':
  parser = argparse.ArgumentParser(description='LINCS Portal REST API client utility')
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
    if not fout: parser.error('ERROR: cannot open outfile: %s'%args.ofile)
  else:
    fout=sys.stdout

  if args.op == 'fetchEntities':
    if not args.searchTerm:
      parser.error('Requires searchTerm.')
      parser.exit()
    FetchEntities(BASE_URL, args.searchTerm, args.facet, fout, args.verbose)

  elif args.op == 'fetchData':
    if not args.searchTerm:
      parser.error('Requires searchTerm.')
      parser.exit()
    FetchData(BASE_URL, args.searchTerm, args.facet, fout, args.verbose)

  elif args.op == 'autoSuggest':
    if not args.searchTerm:
      parser.error('Requires searchTerm.')
      parser.exit()
    Autosuggest(BASE_URL, args.searchTerm, args.facet, fout, args.verbose)

  else:
    parser.error('No operation specified.')
    parser.print_help()

