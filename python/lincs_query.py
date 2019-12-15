#!/usr/bin/env python2
#############################################################################
### LINCS Data Portal  REST API client
###
### http://lincsportal.ccs.miami.edu/dcic/api/fetchentities?searchTerm=Rock1
#############################################################################
### Jeremy Yang
#############################################################################
import sys,os,argparse,re,types
import json,codecs,csv
import urllib2,requests,time
#
import rest_utils_py2 as rest_utils
#
API_HOST="lincsportal.ccs.miami.edu"
API_BASE_PATH="/dcic/api"
API_BASE_URL='http://'+API_HOST+API_BASE_PATH
#
#
#############################################################################
def Autosuggest(base_url,searchTerm,facet,fout,verbose):
  tags=None;
  url=base_url+'/autosuggest?searchTerm=%s'%searchTerm
  rval=rest_utils.GetURL(url,parse_json=True,verbose=verbose)
  print >>sys.stderr, str(rval)
  return

#############################################################################
def FetchData(base_url,searchTerm,facet,fout,verbose):
  tags=None;
  url=base_url+'/fetchdata?searchTerm=%s'%searchTerm
  rval=rest_utils.GetURL(url,parse_json=True,verbose=verbose)
  return

#############################################################################
def FetchEntities(base_url,searchTerm,facet,fout,verbose):
  tags=None;
  url=base_url+'/fetchentities?searchTerm=%s'%searchTerm
  rval=rest_utils.GetURL(url,parse_json=True,verbose=verbose)
  if not rval:
    if verbose:
      print >>sys.stderr, 'not found: %s'%(searchTerm)
    return
  ent = rval
  if not tags:
    tags = ent.keys()
    fout.write(','.join(tags)+'\n')
  vals = [];
  for tag in tags:
    val=(ent[tag] if ent.has_key(tag) else '')
    vals.append(val)
  fout.write(','.join(vals)+'\n')

#############################################################################
if __name__=='__main__':
  parser = argparse.ArgumentParser(
	description='LINCS Portal REST API client utility',
	epilog='.')
  ops = ['fetchEntities','fetchData','autoSuggest']
  parser.add_argument("op",choices=ops,help='operation')
  parser.add_argument("--searchTerm",dest="searchTerm",help="Entity searchTerm e.g. Rock1)")
  parser.add_argument("--i",dest="ifile",help="input file, PubMed IDs")
  parser.add_argument("--facet",dest="facet",help="search facet")
  parser.add_argument("--nmax",type=int,help="max results")
  parser.add_argument("--skip",type=int,help="skip results")
  parser.add_argument("--o",dest="ofile",help="output (CSV)")
  parser.add_argument("-v","--verbose",action="count")

  args = parser.parse_args()

  if args.ofile:
    #fout=open(args.ofile,"w+")
    fout=codecs.open(args.ofile,"w","utf8","replace")
    if not fout: ErrorExit('ERROR: cannot open outfile: %s'%args.ofile)
  else:
    #fout=sys.stdout
    fout=codecs.getwriter('utf8')(sys.stdout,errors="replace")

  if args.op == 'fetchEntities':
    if not args.searchTerm:
      parser.error('Requires searchTerm.')
      parser.exit()
    FetchEntities(API_BASE_URL, args.searchTerm, args.facet, fout, args.verbose)

  elif args.op == 'fetchData':
    if not args.searchTerm:
      parser.error('Requires searchTerm.')
      parser.exit()
    FetchData(API_BASE_URL, args.searchTerm, args.facet, fout, args.verbose)

  elif args.op == 'autoSuggest':
    if not args.searchTerm:
      parser.error('Requires searchTerm.')
      parser.exit()
    Autosuggest(API_BASE_URL, args.searchTerm, args.facet, fout, args.verbose)

  else:
    parser.error('No operation specified.')
    parser.print_help()

