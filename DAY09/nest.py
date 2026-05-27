Students = {
            11: {
                    'name':'john',
                    'location':'Mumbai',
                     'subjects':{'english':40,
                                'french':20,
                                 'maths':90,
                                 'Marathi':80,
                                 }
                 },
            12: {'name':'David','location':'Nagpur',
                 'subjects':{'english':50,
                             'french': 30,
                             'maths': 80,
                             'Marathi':70,
                             }
                 },
            13:{'name':'Prakash',
                'location':'Delhi',
                'subjects':{'english':66,
                            'french': 47,
                            'maths': 89,
                            'Marathi':77,
                            }

                },
            14:{'name':'Jacob','location':'Pune',
                'subjects':{'english':80,
                            'french': 30,
                            'maths': 99,
                            'Marathi':80,}
                },

            15:{'name':'Krish','location':'Nashik',
                'subjects':{'english':90,
                            'french': 35,
                            'maths': 90,
                            'Marathi':86,
                            }
                },
            }
print(Students.keys())
print(Students.values())
for roll_no, info in Students.items():
    print(f"{roll_no}: {info}")
print(Students)
print(Students[15])
print(Students[11]['name'])
print(Students[13]['location'])
print(Students[12]['name'],Students[12]['location'])
print(Students[14]['subjects'])
