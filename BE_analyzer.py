import sys

fn = sys.argv[1]

depth_cutoff = 50

with open(fn) as f, open(f'result_C_to_T_{fn}.txt', 'w') as fw:
	fw.write('Chro\tPos\tDepth\tCtoT_count\t(%)\n')
	next(f)
	for line in f:
		line = line.split('\t')
		ref_nt = line[2]
		depth = int(line[4])
		if ref_nt not in 'CG' or depth < depth_cutoff:
			continue
		chro = line[0]
		position = line[1]
		mut_list = line[6].replace('[','').replace(']','').split(', ')
		mut_cnt = 0
		if ref_nt == 'C':
			mut_cnt = int(mut_list[3])
		elif ref_nt == 'G':
			mut_cnt = int(mut_list[0])
		per = round(mut_cnt*100/depth, 3)
		fw.write(f'{chro}\t{position}\t{depth}\t{mut_cnt}\t{per}\n')
	
