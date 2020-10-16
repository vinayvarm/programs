with open('sample','r') as rf:
    with open('samplecopy','w') as wf:
        for line in rf:
            wf.write(line)
