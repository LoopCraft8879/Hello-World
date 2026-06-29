table={
    ('A','Dirty'):'Suck',
    ('A','Clean'):'Right',
    ('B','Dirty'):'Suck',
    ('B','Clean'):'Left',
    }
def table_driven_agent(percept):
    return table.get(percept,"No Action")
percepts=[
    ('A','Dirty'),
    ('A','Clean'),
    ('B','Dirty'),
    ('B','Clean'),
    ]
for percept in percepts:
    action=table_driven_agent(percept)
    print("Percept:",percept,"->Action:",action)
    
