def parse_file(f):
    lines = f.readlines()
    idx = 0
    c = int(lines[idx].split()[0])
    p = int(lines[idx].split()[1])
    idx=idx+1
    contribs = {}
    contrib_skills = {}
    for i in range(c):
        contrib = lines[idx].split()[0]
        contribs[i] = contrib
        nb_skills = int(lines[idx].split()[1])
        idx=idx+1
        j=0 
        skills = []
        while j < nb_skills:
            idx=idx+j
            skill = {}
            skill[lines[idx].split()[0]] = int(lines[idx].split()[1])
            skills.append(skill)
            j+=1
        contrib_skills[i] = skills
        idx = idx + 1

    projects = {}
    for k in range(p):
        line_project = lines[idx].split()
        name_project = line_project[0]
        di = int(line_project[1])
        si = int(line_project[2])
        bi = int(line_project[3])
        ri = int(line_project[4])
        idx=idx+1
        l=0 
        skills = []
        while l < ri:
            idx=idx+l
            skill = {}
            skill[lines[idx].split()[0]] = int(lines[idx].split()[1])
            skills.append(skill)
            l+=1
        project = {
            "name":name_project,
            "di":di,
            "si":si,
            "bi":bi,
            "ri":ri,
            "skills":skills
        }
        projects[k] = project  
        idx = idx + 1

    return contribs,contrib_skills,projects