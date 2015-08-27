from particleWorkflow import particleFilter

x = particleFilter()
print x.next()
print x.send([1,2,3,4])
print x.next()
print x.send([1,2,3,4])
