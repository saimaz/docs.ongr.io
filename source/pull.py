# -- autopull repos

import string

lines = [line.strip() for line in open('%s/sources/.repos' % (os.path.dirname(os.path.realpath(__file__))))]

for line in lines:
    if ( line[0]!="#" ) :
        repository_url, doc_directory = string.split(line, ' ')
        if doc_directory == '~':
            doc_directory = 'Resources/doc'

        os.system("cd sources; mkdir %s; cd %s; git init; git remote add -f origin %s; git config core.sparsecheckout true; echo '%s' > .git/info/sparse-checkout; echo 'Resources/API' >> .git/info/sparse-checkout; git pull origin master;" % (repository_url.split("/")[-1], repository_url.split("/")[-1], repository_url, doc_directory))

# fix links to githubs' .rst files.
os.system("grep -rl '.rst' sources/ | grep -v '/.git/' | xargs perl -pe 's/\`(.*)<(.*)\.rst>\`_/$1:doc:`$2`/g' -i")
