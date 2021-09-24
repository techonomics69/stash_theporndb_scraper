
def sceneQuery(query_in: str) -> str:
    # implement your own logic here
    # This is primarily useful if you have a group of files that
    #   do not conform to the standard naming scheme
    #
    # For example here's my code to search on the LegalPorno scene ID and date
    #
    # ~ import re
    # ~ def sceneQuery(query_in: str) -> str:
        # ~ sceneid = ''
        # ~ if re.search('legal ?porno', query_in.lower()):
            # ~ if re.search(' (\d{4}-\d{2}-\d{2}) ', query_in):
                # ~ scenedate = re.search(' (\d{4}-\d{2}-\d{2}) ', query_in).group(1) + "%20"
            # ~ else:
                # ~ scenedate = ''
            # ~ if re.search('([a-zA-Z]{2,3}\d{3,4})', query_in):
                # ~ sceneid = re.search('([a-zA-Z]{2,3}\d{3,4})', query_in).group(1).strip()
                
        # ~ if sceneid:
            # ~ url = "https://api.metadataapi.net/api/scenes?q=" + scenedate + sceneid    
            # ~ return url

    
    return query_in
