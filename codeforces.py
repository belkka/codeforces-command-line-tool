import click
import os

from codeforces_api import contest_standings


@click.group()
def cli():
    pass


@cli.command('contest_info', help='Getting contest info with with given contest id')
@click.argument('contest_id') # help='Contest id given from contest URL')
def contest_info(contest_id):
    standings = contest_standings(contestId=contest_id)
    contest_name = standings['contest']['name']
    print(contest_name)
    for problem in standings['problems']:
        print("\t{0[index]}. {0[name]}".format(problem))


@cli.command('init_dir', help='Initialize dir with given contest id')
@click.argument('contest_id')
@click.option('--folder_format', default='{0[index]}. {0[name]}', help='Format for creating directory.')
@click.option('--cmake_gen', default=False, help='Specify create or not CMakeLists.txt for creating project.')
@click.option('--create_source', default=False, help='Create sample source, or not')
@click.option('--source_format', default='{0[index]}.cpp', help='Source file format.')
def init_dir(contest_id, folder_format, cmake_gen, create_source, source_format):
    standings = contest_standings(contestId=contest_id)
    contest = standings['contest']

    os.mkdir(contest['name'])
    os.chdir(contest['name'])
    if cmake_gen: 
        cmake_lists = open('CMakeLists.txt', 'w')

    for problem in standings['problems']:
        folder = folder_format.format(problem)
        os.mkdir(folder)
        
        if cmake_gen: cmake_lists.write('add_subdirectory("{}")\n'.format(folder))
        if create_source: 
            source = source_format.format(problem)
            open(folder + '/' + source, 'w').write('')
        if cmake_gen and create_source:
            open(folder + '/CMakeLists.txt', 'w').write('add_executable({0[index]} {1})'.format(problem, source))


if __name__ == '__main__':
    cli()

