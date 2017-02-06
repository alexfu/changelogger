import click
import re

@click.command()
@click.argument('file', type=click.Path(exists=True))
@click.argument('tag')
@click.option('--output', type=click.Path(dir_okay=False), help='Output file')
@click.version_option(message='%(prog)s version %(version)s')
def cli(file, tag, output):
    inputFile = click.open_file(file, 'r')
    fileContent = readFileContents(inputFile)
    changes = processChangelog(fileContent.splitlines(), tag)
    changes_string = '\n'.join(changes)
    if output:
        outputFile = click.open_file(output, 'w')
        outputFile.write(changes_string)
    else:
        click.echo(changes_string)

def readFileContents(file):
    content = ""
    while True:
        chunk = file.read(1024)
        if chunk:
            content += chunk
        else:
            break
    return content

def processChangelog(changelog, tag):
    subchangelog = []
    pattern = '\[' + tag + '\]\(.*\)'
    copy = False
    for line in changelog:
        match = re.search(pattern, line)
        if match:
            if copy:
                copy = False
                break
            else:
                pattern = re.split('\s', line)[0]
                copy = True
        elif copy:
            subchangelog.append(line)
    return extractChanges(subchangelog)

def extractChanges(changelog):
    changes = []
    for line in changelog:
        if line and line[0] == '-':
            changes.append(sanitizeChange(line))
    return changes

def sanitizeChange(change):
    pattern = '(\[.*\]\(.*\))'
    result = re.search(pattern, change)
    change = change[0:result.span()[0]]
    change = change.strip()
    return change
