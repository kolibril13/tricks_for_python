from pathlib import Path
outpath = Path.cwd() / 'output' / 'output.xlsx'
outpath1 = Path.cwd() / 'output/output.xlsx'

subfolder = Path('output/output.xlsx')
outpath2 = Path.cwd() / subfolder

print(outpath)
print(outpath1)
print(outpath2)