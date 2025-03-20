import pickle
def StuRegister():
    print('Registration')
    f=open('Login.dat','ab')
    name=input('Enter name: ')
    ID=input('Enter ID: ')
    pn=int(input('Enter pincode:'))
    passw=input('Create password: ')
    passw2=input('Confirm password: ')
    while passw2!=passw:
        print('Wrong password. Please retry.')
        passw2=input('Confirm password: ')
    AddStu(name, ID, pn)
    pickle.dump([ID, passw, name], f)
    f.close()
    name1=''
    for i in name.split():
        name1+=i
    
    import mysql.connector as sq
    con=sq.connect(host='localhost',user='root',passwd='root',database='CS_Project')
    cur=con.cursor()
    qr="create table {}(Chapter_Name varchar(40), Marks_Scored int,Total_Marks int);".format(name1)
    cur.execute(qr)
    con.commit()
    cur.close()
    StuMain()

def TeaRegister():
    print('Registration')
    f=open('Login.dat','ab')
    name=input('Enter name: ')
    ID=input('Enter ID: ')
    pn=int(input('Enter pincode:'))
    passw=input('Create password: ')
    passw2=input('Confirm password: ')
    while passw2!=passw:
        print('Wrong password. Please retry.')
        passw2=input('Confirm password: ')
    pickle.dump([ID, passw, name], f)
    f.close()
    TeaMain()

def AddStu(name,ID,pincode):
    import mysql.connector as sq
    conn=sq.connect(host='localhost', user='root', passwd='root', database='CS_Project')
    cur=conn.cursor()
    rn=int(input("Enter Roll number: "))
    pn=int(input("Enter Phone number: "))
    d=input("Enter Date of Birth: ")
    qr= "insert into Student_Record (Name, Roll_Number, Phone_Number, Email_ID, Pincode, DOB) \ values('{}', {}, {}, '{}', {}, '{}')".format(name, rn, pn, ID, pincode, d)
    cur.execute(qr)
    conn.commit()
    conn.close()

def TeaLogin():
    f=open('Login.dat','rb')
    ID=input('Enter Teacher ID: ')
    code=int(input("Enter Teacher's code: "))
    passw=input('Enter password: ')
    try:
        while True:
            r=[]
            r=pickle.load(f)
            if r[0]==ID:
                while r[1]!=passw:
                    print('Wrong password. Please try again.')
                    passw=input('Enter password:')
    except EOFError:
        print(' ')
    TeaMain()

def StuLogin():
    f=open('Login.dat','rb')
    ID=input('Enter Student ID: ')
    code=int(input("Enter Student's code: "))
    passw=input('Enter password: ')
    try:
        while True:
            r=[]
            r=pickle.load(f)
            if r[0]==ID:
                while r[1]!=passw:
                    print('Wrong password. Please try again.')
                    passw=input('Enter password:')
    except EOFError:
        print(' ')
    StuMain()

def StuProgress(name):
    import mysql.connector as sq
    con=sq.connect(host='localhost',user='root',passwd='root',database='CS_Project')
    cur=con.cursor()
    qr='select * from {};'.format(name)
    cur.execute(qr)
    d=cur.fetchall()
    F="%15s %15s %15s"
    print(F%("Chapter","Marks Scored","Total Marks"))
    print("="*125)
    for i in d:
        for j in i:
            print("%14s"%j, end='')
        print()
    print("="*125)
            
def GetScores(name1):
    name=''
    for i in name1.split():
        name+=i
        import mysql.connector as sq
        con=sq.connect(host='localhost',user='root',passwd='root',database='CS_Project')
        cur=con.cursor()
        qr='select Chapter_Name, Marks_Scored from {}'.format(name)
        cur.execute(qr)
        data=cur.fetchall()
        for i in data:
            ProgressGraph(i[0],i[1])

Chapters = []
Y_individual_score = []
Z_total_score = []

def ProgressGraph(chapter,score):
    import numpy as np
    import matplotlib.pyplot as plt
    Chapters.append(chapter)
    Y_individual_score.append(score*10)
    Z_total_score.append(100)
    X_axis = np.arange(len(Chapters))
    plt.bar(X_axis - 0.0, Z_total_score, 0.5, label = 'Total')
    plt.bar(X_axis + 0.0, Y_individual_score, 0.5, label ='Individual Score')
    plt.xticks(X_axis, Chapters)
    plt.xlabel("Chapters")
    plt.ylabel("Score")
    plt.title("Chapter Wise Score")
    plt.legend()
    plt.show()

def StuDetails():
    import mysql.connector as sq
    conn=sq.connect(host='localhost',user='root',passwd='root',database='CS_Project')
    cur=conn.cursor()
    qr='Select * from Student_Record'
    cur.execute(qr)
    print('Name','Roll No.','Phone No.','EMail ID','PINCode','DOB',sep=' '*5)
    data=cur.fetchall()
    for i in data:
        print('='*80)
        for j in i:
            print(j,end=' '*5)
        print()
    conn.commit()
    conn.close()

def AddScores(Name, Chapter, Marks, Total_Marks):
    import mysql.connector as sq
    con=sq.connect(host='localhost',user='root',passwd='root',database='CS_Project')
    cur=con.cursor()
    qr="insert into {} values('{}',{},{});".format(Name, Chapter, Marks, Total_Marks)
    cur.execute(qr)
    con.commit()
    cur.close()

def RayOpticsQuiz():
    score=0
    ans={1:'b',2:'c',3:'a',4:'a',5:'c',6:'a',7:'d',8:'b',9:'b',10:'a'}
    question={1:'''Question 1.
\nAir bubble in water behaves as
\n(a) sometimes concave, sometimes convex lens
\n(b) concave lens
\n(c) convex lens
\n(d) always refracting surface''', 
2:'''Question 2.
\nA converging lens is used to form an image on a screen. When the
upper half of the lens is covered by an opaque screen.
\n(a) half the image will disappear.
\n(b) incomplete image will be formed.
\n(c) intensity of image will decrease but complete image is formed.
\n(d) intensity of image will increase but image is not distinct.''',
3:'''Question 3.
\nIn optical fibres, the refractive index of the core is
\n(a) greater than that of the cladding.
\n(b) equal to that of the cladding.
\n(c) smaller than that of the cladding.
\n(d) independent of that of cladding.''', 
4:'''Question 4.
\nWhen a ray of light enters from one medium to another, then which
of the following does not change?
\n(a) Frequency
\n(b) Wavelength
\n(c) Speed
\n(d) Amplitude''', 
5:'''Question 5.
\nThe astronomical telescope consists of objective and eyepiece. The
focal length of the objective is
\n(a) equal to that of the eyepiece.
\n(b) shorter than that of eyepiece.
\n(c) greater than that of eyepiece.
\n(d) five times shorter than that of eyepiece.''',
6:'''Question 6.
\nWhich of the following phenomena is used in optical fibres ?
\n(a) Total internal reflection
\n(b) Scattering
\n(c) Diffraction
\n(d) Refraction''', 
7:'''Question 7.
\nCritical angle of light passing from glass to water is minimum for
\n(a) red colour
\n(b) green colour
\n(c) yellow colour
\n(d) violet colour''', 
8:'''Question 8.
\nIf a glass prism is dipped in water, its dispersive power
\n(a) increases
\n(b) decreases
\n(c) does not change
\n(d) may increase or decrease depending on whether the angle of the
prism is less than or greater than 60o''', 
9:'''Question 9.
\nTo increase the angular magnification of a simple microscope, one
should increase
\n(a) the focal length of the lens
\n(b) the power of the lens
\n(c) the aperture of the lens
\n(d) the object size''', 
10:'''Question 10.
\nWhich of these statements is correct about the rainbow?
\n(a) In the primary rainbow, red colour is on the outside and violet
colour is on the inside.
\n(b) In the primary rainbow, violet colour is on the outside and red
colour is on the inside.
\n(c) In the secondary rainbow, the light wave suffers one total
internal reflection before coming out.
\n(d) The secondary rainbow is brighter than the primary rainbow.'''}

    for i in range(1,11):
        print(question[i])
        print()
        a=input('Answer:')
        if a.lower()==ans[i]:
            print()
            print('CORRECT!')
            print()
            print('='*125)
            print()
            score+=1
        else:
            print()
            print('WRONG :( ')
            print()
            print('='*125)
            print()

    print()
    print('Your score is:',score,'/10')
    AddScores(Name, 'Ray Optics', score, 10)

def WaveOpticsQuiz():
    score=0
    ans={1:'a',2:'d',3:'d',4:'b',5:'c',6:'a',7:'c',8:'d',9:'d',10:'c'}
    question={1:'''Question 1.
\nWhat happens if one of the slits, say S1 in Young’s double slit
experiment is covered with a glass plate which absorbs half the
intensity of light from it?
\n(a) The bright fringes become less-bright and the dark fringes have
a finite light intensity
\n(b) The bright fringes become brighter and the dark fringes become
darker
\n(c) The fringe width decreases
\n(d) No fringes will be observed''', 
2:'''Question 2.
\nWhat happens to the interference pattern the two slits S1 and S2 in
Young’s double experiment are illuminated by two independent but
identical sources?
\n(a) The intensity of the bright fringes doubled
\n(b) The intensity of the bright fringes becomes four times
\n(c) Two sets of interference fringes overlap
\n(d) No interference pattern is observed''', 
3:'''Question 3.
\nWhat is the reason for your answer to the above question?
\n(a) The two sources do not emit light of the same wavelength
\n(b) The two sources emit waves which travel with different speeds
\n(c) The two sources emit light waves of different amplitudes
\n(d) There is not constant phase difference between the waves
emitted by the two sources''', 
4:'''Question 4.
\nA single slit diffraction pattern is obtained using a beam of red
light. What happens if the red light is replaced by the blue light?
\n(a) There is no change in diffraction pattern
\n(b) Diffraction fringes become narrower and crowded
\n(d) Diffraction fringes become broader and farther apart
\n(d) The diffraction pattern disappear''', 
5:'''Question 5.
\nWhen a polaroid is rotated, the intensity of light varies but never
reduces to zero. It shows that the incident light is:
\n(a) unpolarised
\n(b) completely plane polarised
\n(c) partially plane polarised
\n(d) None of the above''', 
6:'''Question 6.
\nWhen a polaroid is rotated, the intensity of light does not vary.
The incident light may be:
\n(a) unpolarised
\n(b) completely polarised
\n(c) partially plane polarised
\n(d) None of the above''', 
7:'''Question 7.
\nFor sustained interference, we need two sources which
emit radiations :
\n(a) of the same intensity
\n(b) of the same amplitude
\n(c) having a constant phase difference
\n(d) None of these''', 
8:'''Question 8.
\nTwo sources of light are said to be coherent when both give out
light waves of the same:
\n(a) amplitude and phase
\n(b) intensity and wavelength
\n(c) speed
\n(d) wavelength and a constant phase difference''',
9:'''Question 9.
\nThe intensity of light emerging from the two slits in Young’s
experiment is in the ratio 1 : 4.
The ratio of,the intensity of the minimum to that of the consecutive
maximum will be:
\n(a) 1 : 4
\n(b) 1 : 9
\n(c) 1 : 16
\n(d) 2 : 3''', 
10:'''Question 10.
\nThe angle of minimum deviation of a prism depends upon the aggie
of:
\n(a) incidence
\n(b) reflection
\n(c) prism
\n(d) none of these'''}
    
    for i in range(1,11):
        print(question[i])
        print()
        a=input('Answer:')
        if a.lower()==ans[i]:
            print()
            print('CORRECT!')
            print()
            print('='*125)
            print()
            score+=1
        else:
            print()
            print('WRONG :( ')
            print()
            print('='*125)
            print()

    print()
    print('Your score is:',score,'/10')
    AddScores(Name, 'Wave Optics', score, 10)

def SemiconductorsQuiz():
    score=0
    ans={1:'a',2:'c',3:'b',4:'a',5:'c',6:'c',7:'c',8:'c',9:'b',10:'c'}
    question={ 1:'''Question 1.
\n A semiconductor is formed by ......... bonds.
\n(a) Covalent
\n(b) Electrovalent
\n(c) Co-ordinate
\n(d) None of the above''', 
2:'''Question 2.
\n Semiconductor has ............ temperature coefficient of resistance.
\n(a) Positive
\n(b) Zero
\n(c) Negative
\n(d) None of the above''', 
3:'''Question 3.
\n The most commonly used semiconductor is ......... .
\n(a) Germanium
\n(b) Silicon
\n(c) Carbon
\n(d) Sulphur''', 
4:'''Question 4.
\n If the conductivity of a semiconductor is only due to break of the
covalent band due to the thermal excitation, then the semiconductor
is called:
\n (a) intrinsic
\n (b) extrinsic
\n (c) Acceptor
\n (d) none of these''', 
5:'''Question 5.
\n A hole in a p-type semiconductor is-
\n (a) an excess electron
\n (b) A missing atom
\n (c) A missing electron
\n (d) A donor level''', 
6:'''Question 6.
\n The mobility of conduction electrons is greater than that of holes
since electrons is greater than that of holes since electrons.
\n (a) are negatively charged.
\n (b) are lighter
\n (c) require smaller energy for moving through the crystal lattice.
\n (d) Undergo smaller number of collisions.''', 7:'''Question 7.
\n The conductivity of semiconductors like Ge and Si:
\n (a) increases when it is doped with pentavalent impurity.
\n (b) increases when it is doped with trivalent impurity.
\n (c) increases when it is doped with pentavalent or trivalent
impurity.
\n (d) none''', 
8:'''Question 8.
\n Which of following statements is not true?
\n (a) Resistance of an intrinsic semiconductor decreases with
increase in temperature.
\n (b) Doping pure Si with trivalent impurities gives p-type
semiconductor.
\n (c) The majority carriers in n-type semiconductor are holes.
\n (d) A p-n junction can act as semiconductor diode.''',
9:'''Question 9.
\n Electrical conductivity of a semiconductor
\n (a) decreases with the rise in its temperature.
\n (b) increases with the rise in its temperature.
\n (c) does not change with the rise in its temperature.
\n (d) first increases and then decreases with the rise in its
temperature.''', 
10:'''Question 10.
\n A n-type semiconductor is:
\n (a) negatively charged.
\n (b) positively charged.
\n (c) neutral.
\n (d) none of these.'''}
    
    for i in range(1,11):
        print(question[i])
        print()
        a=input('Answer:')
        if a.lower()==ans[i]:
            print()
            print('CORRECT!')
            print()
            print('='*125)
            print()
            score+=1
        else:
            print()
            print('WRONG :( ')
            print()
            print('='*125)
            print()

    print()
    print('Your score is:',score,'/10')
    AddScores(Name,'Wave Optics', score, 10)

def DualNatureQuiz():
    score=0
    ans={1:'d', 2:'a',3:'a',4:'b',5:'a',6:'b',7:'d',8:'a',9:'b',10:'d'}
    question={ 1:'''Question 1.
\n In nuclear reactors, the control rods are made of
\n (a) cadmium
\n (b) graphite
\n (c) krypton
\n (d) plutonium''', 
2: '''Question 2.
\n When the mass of a sample of a radioactive substance decreases,
the mean life of the sample:
\n (a) increases
\n (b) decreases
\n (c) remain unchanged
\n (d) first decreases then increases''', 
3:'''Question 3.
\n The work function of photoelectric material is 3.3 eV. The
threshold frequency will be equal to:
\n (a) 1 kg
\n (b) 0.01 kg
\n (c) 3.84 kg
\n (d) 0.384 kg ''', 
4:'''Question 4.
\n The strength of photoelectric current depends upon :
\n (a) angle of incident radiation
\n (b) frequency of incident radiation
\n (c) intensity of incident radiation
\n (d) distance between anode and cathode''', 
5: '''Question 5.
\n In photoelectric emission, for alkali metals the threshold
frequency lies in the:
\n (a) visible region
\n (b) ultraviolet region
\n (c) infrared region
\n (d) far end of the infrared region''', 
6:'''Question 6.
\nWhat is the de-Broglie wavelength of an electron accelerated from
rest through a potential difference of 100 volts?
\n (a) 12.3 Å
\n (b) 1.23 Å
\n (c) 0.123 Å
\n (d) None of these ''', 
7:'''Question 7.
\n The different stages of discharge in a discharge tube can be
explained on the basis of:
\n (a) the wave nature of light
\n (b) the dual nature of light
\n (c) wave nature of electrons
\n (d) the collision between the charged particles emitted from the
cathode the atoms of the gas in the tube''', 
8:'''Question 8.
\n When an electron jumps across a potential difference of 1 V, it
gains energy equal to :
\n (a) 1.602 × 10-19 J
\n (b) 1.602 × 1019 J
\n (c) 1.602 × 1024 J
\n (d) 1 J''', 
9:'''Question 9.
\n Which of the following radiations cannot eject photo electrons?
\n (a) ultraviolet
\n (b) infrared
\n (c) visible
\n (d) X-rays''', 
10:''' Question 10.
\n X-rays are:
\n (a) deflected by an electric field
\n (b) deflected by a magnetic field
\n (c) deflected by both electric and magnetic fields
\n (d) not deflected by electric and magnetic fields'''}
    
    for i in range(1,11):
        print(question[i])
        print()
        a=input('Answer:')
        if a.lower()==ans[i]:
            print()
            print('CORRECT!')
            print()
            print('='*125)
            print()
            score+=1
        else:
            print()
            print('WRONG :( ')
        print()
        print('='*125)
        print()
        
    print()
    print('Your score is:',score,'/10')
    AddScores(Name, 'Dual Nature of Radiation & Matter', score, 10)

def AtomsQuiz():
    score=0
    ans={1:'c', 2:'c',3:'c',4:'c',5:'a',6:'d',7:'a',8:'c',9:'d',10:'b'}
    question={ 1:'''Question 1.
\n If 13.6 eV energy is required to ionise the hydrogen atom, then
energy required to remove an electron from n = 2 is
\n (a) 10.2 eV
\n (b) 0 eV
\n (c) 3.4 eV
\n (d) 6.8 eV.''', 
2:'''Question 2.
\n 15. The first model of atom in 1898 was proposed by
\n (a) Ernst Rutherford
\n (b) Albert Einstein
\n (c) J.J. Thomson
\n (d) Niels Bohr ''', 
3: '''Question 3.
\n 3. In Bohr’s model, the atomic radius of the first orbit is rQ.
Then, the radius of the third orbit is
\n (a) r0/9
\n (b) r0
\n (c) 9r0
\n (d) 3r0 ''', 
4:'''Question 4.
\n The ratio between Bohr radii is
\n (a) 1 : 2 : 3
\n (b) 2 : 4 : 6
\n (c) 1 : 4 : 9
\n (d) 1 : 3 : 5 ''', 
5:'''Question 5.
\n The longest wavelength in Balmer series of hydrogen spectrum will
be
\n (a) 6557 Å
\n (b) 1216 Å
\n (c) 4800 Å
\n (d) 5600 Å ''', 
6:'''Question 6.
\n The ionisation energy of hydrogen atom is 13.6 eV. Following
Bohr’s theory the energy corresponding to a transition between 3rd
and 4th orbits is
\n (a) 3.40 eV
\n (b) 1.51 eV
\n (c) 0.85 eV
\n (d) 0.66 eV ''', 
7:'''Question 7.
\n On moving up in the energy states of a H-like atom, the energy
difference between two consecutive energy states
\n (a) decreases.
\n (b) increases.
\n (c) first decreases then increases.
\n (d) first increases then decreases. ''', 
8:'''Question 8.
\n The transition of electron from n = 4, 5, 6, .......... to n = 3
corresponds to
\n(a) Lyman series
\n(b) Balmer series
\n(c) Paschen series
\n(d) Brackettseries ''', 
9:'''Question 9.
\n As per Bohr model, the minimum energy (in eV) required to remove
an electron from the ground state of double ionized Li atom (Z = 3)
is
\n (a) 1.51 eV
\n (b) 13.6 eV
\n (c) 40.8 eV
\n (d) 122.4 eV ''', 
10:'''Question 10.
\n Which of the following spectral series in hydrogen atom gives
spectral line of 4860 A?
\n (a) Lyman
\n (b) Balmer
\n (c) Paschen
\n (d) Brackett ''' }
    
    for i in range(1,11):
        print(question[i])
        print()
        a=input('Answer:')
        if a.lower()==ans[i]:
            print()
            print('CORRECT!')
            print()
            print('='*125)
            print()
            score+=1
        else:
            print()
            print('WRONG :( ')
            print()
            print('='*125)
            print()
    print()
    print('Your score is:',score,'/10')
    AddScores(Name, 'Atoms', score, 10)

def NucleiQuiz():
    score=0
    ans={1:'a', 2:'c',3:'d',4:'a',5:'d',6:'d',7:'d',8:'c',9:'a',10:'c'}
    question={ 1:'''Question 1.
\n In nuclear reactors, the control rods are made of
\n (a) cadmium
\n (b) graphite
\n (c) krypton
\n (d) plutonium''', 
2: '''Question 2.
\n When the mass of a sample of a radioactive substance decreases,
the mean life of the sample:
\n (a) increases
\n (b) decreases
\n (c) remain unchanged
\n (d) first decreases then increases''', 
3:'''Question 3.
\n A nuclear explosive is designed to deliver 1 MW power in the form
of heat energy.
\n If the explosion is designed with nuclear fuel consisting of U235
to run a reactor at this power level
\n for one year, then the amount of fuel needed is (given energy per
fission is 200 MeV)
\n (a) 1 kg
\n (b) 0.01 kg
\n (c) 3.84 kg
\n (d) 0.384 kg ''', 
4:'''Question 4.
\n Particles which can be added to the nucleus of an atom without
changing its chemical properties are called
\n (a) neutrons
\n (b) electrons
\n (c) protons
\n (d) alpha particles''', 
5: '''Question 5.
\n The neutron was discovered by whom?
\n (a) Marie Curie
\n (b) Pierre Curie
\n (c) Rutherford
\n (d) James Chadwick''', 
6:'''Question 6.
\n The mass of an atomic nucleus is less than the sum of the masses
of its constituents. This mass defect is converted into
\n (a) heat energy
\n (b) light energy
\n (c) electrical energy
\n (d) energy which binds nucleons together ''', 
7:'''Question 7.
\n In nuclear reaction, there is conservation of
\n (a) mass only
\n (b) energy only
\n (c) momentum only
\n (d) mass, energy and momentum''', 
8:'''Question 8.
\n In nuclear reaction, there is conservation of
\n (a) mass only
\n (b) energy only
\n (c) momentum only
\n (d) mass, energy and momentum''', 
9:'''Question 9.
\n For a radioactive material, half-life is 10 minutes. If initially
there are 600 number of nuclei,
\n the time taken (in minutes) for the disintegration of 450 nuclei
is:
\n (a) 20
\n (b) 10
\n (c) 30
\n (d) 15''', 
10:''' Question 10.
\n For a nuclear fusion process, suitable nuclei are
\n (a) any nuclei
\n (b) heavy nuclei
\n (c) lighter nuclei
\n (d) nuclei lying in the middle of periodic table'''}
    
    for i in range(1,11):
        print(question[i])
        print()
        a=input('Answer:')
        if a.lower()==ans[i]:
            print()
            print('CORRECT!')
            print()
            print('='*125)
            print()
            score+=1
        else:
            print()
            print('WRONG :( ')
            print()
            print('='*125)
            print()
    print()
    print('Your score is:',score,'/10')
    AddScores(Name, 'Nuclei', score, 10)

#Ray Optics Formulae
def RayOpticsFormulae():
    print('='*125)
    formulae = { 1:'''Refractive Index = Speed of light in
vacuum/Speed of light in medium''' ,

2:'''Snell's Law (μ) = sin i / sin r''',
3:'''Mirror formula =1/f = 1/v + 1/u = 2/r''',
4:'''Total Internal Reflection (c) μ = 1/sin C''',
5:'''Refraction at a concave surface = μ2/v – μ1/u = μ2

- μ1/R''',

6:'''Refraction at a convex surface producing real

image= μ2/v – μ1/u = μ2 - μ1/R''',

7:'''Refraction at a convex surface producing virtual

image = μ2/v – μ1/u = μ2 - μ1/R ''',

8:'''Convex surface producing a real image of a real

object = μ2/u – μ1/v = μ2 - μ1/R''',

9:'''Light travelling from air to glass= μ/v – 1/u =

μ-1/R''',

10:'''Light travelling from glass to air = μ/u – 1/v =

μ-1/R'''}
    
    for key, value in formulae.items():
        print(key, ':', value)
        print('='*125)

#semi-conductors formulae
def SemiconductorsFormulae():
    print('='*125)
    formulae = {1:'''Rectifier efficiency = dc output power / ac input
power''',

2:'''Intrinsic Semiconductors ne = nn =ni ''',
3:'''Extrinsic Semiconductors ne ≃ Nd >nn (n-type) nn ≃

Nd >ne (p-type)''',

4: '''Mobility μ = Vd/E''',

5: '''Action of Transistor IE=IC+IB ''',
6:'''Relations between α and β α = β/(1+β) β = α/(1-α)

''',

7: '''Voltage gain of an amplifier is given by Av= V0/Vi

''',

8: '''Av = β (Routput/Rinput) ''',
9: '''Number of electrons reaching from the valence band

to conduction band ղ = AT^3/2 x e^-Eg/2kT ''',

10: '''Undoped semiconductor n = p = ni '''}

    for key, value in formulae.items():
        print(key, ' : ', value)
        print('='*125)

# Wave Optics Formula
def WaveOpticsFormulae():
    formulae = {1:'''Speed v of a wave = v = lambda / T ''',
2:'''Doppler Effect = ∆v /vo = -v/c''',
3:'''Relation between phase difference & path difference

= 2 pi / lambda * ∆x ''',

4:'''Young’s double slit interference experiment: Fringe

width= w = D lambda / d ''',

5:'''Destructive interference: Phase difference = (n +

1⁄2)2 pi, where n is an integer''',

6:'''Intensity of the light due to polarization= I =

Io cos^2theta''',

7:'''Brewster’s Law: = tan theta p ''',
8:'''Angular spread of the central maxima= 2 lambda / d

''',

9:'''Width of the central maxima: 2 lambda D / d''',
10:'''Path difference= x = n lambda '''}

    print('='*125)
    for key, value in formulae.items():
        print(key, ' : ', value)
        print('='*125)
    
#Dual Nature formula
def DualNatureFormulae():
    formulae = {1:'''The stopping potential is directly related to the
maximum kinetic energy of electrons emitted= e V0 = (1/2) m v^2 max =
Kmax''',

2:'''Energy (E) of a photon is given by: E = hv =

hc/λ''',

3:'''Kmax = eVo = hν - Φo Vo = (h/e)v + (Φo/e)''',

4:'''Momentum (p) of a photon is given by: p = hv/c =

h/λ ''',

5:'''de Broglie wavelength of a particle of mass m

moving with velocity v is given by λ= h/p=h/mv ''',

6:'''No of photons emitted n =power/energy ''',
7:'''De broglie wavelength gas molecule λ=h/mcrms =

h/3mKT''',

8:'''Einstein’s Photoelectric Equation: 1/2mv2

max=h(v-vo) ''',

9:'''The kinetic mass of a photon is, m=E/c^2 = h/cλ

''',

10:'''Heisenberg’s Uncertainty Principle ∆ x ∆P ≥ (h /
4π) '''}
    
    print('='*125)
    for key, value in formulae.items():
        print(key, ' : ', value)
        print('='*125)
    
#Atoms Formulae
def AtomsFormulae():
    formulae = {1:'''Rutherford's Scattering Forrmula N(0)=Ni
ntZ^2e^4/(8πε0)^2r^2E^2sin^4(0/2)''',

2:'''De-Broglie wavelength: λ=h/mc =h/p ( for photon

)''',

3:'''Radius of orbit of electron is given by r=n2h2 /4π2

mK Ze2 ⇒r∝n2 /Z ''',

4:'''Total energy of electron in any orbit is given by E
= – 2π2 me4 Z2 K2 / n2 h2 = – 13.6 Z2 / n2 eV ⇒Ep =∝Z2 /n2''',
5:'''Velocity of electron in any orbit is given by v =

2π KZe2 / nh ⇒ v ∝ Z / n''',

6:'''Frequency of electron in any orbit is given by v =

KZe2 / nhr = 4π2 Z2 e4 mK2 / n3 h3 ''',

7:'''Kinetic energy of electron in any orbit is given by

Ek = 2π 2me 4Z2K2 / n2 h2 = 13.6 Z2 / n2 eV ''',

8:'''Potential energy of electron in any orbit is given
by Ep = –4π2 me4 Z2 K2 /n2 h2 =27.2Z2 /n2 eV ⇒Ep =∝Z2 /n2''',
9:'''Bohr quantization principle mvr=nh/2π 2πr=nλ''',
10:'''Wave number= v = 1/λ = R[1/n1^2 - 1/n2^2] '''}

    for key, value in formulae.items():
        print(key, ' : ', value)

#Nuclei formula
def NucleiFormulae():
    formulae = {1:'''d = √2hR where R = radius of earth''',

2: '''d = √2Rhr + √2RhR, where hT, hR are the heights of

transmitter and receiver antennas''',

3:'''Population covered = population density x area

covered''',

4:'''N = total bandwidth of channels / bandwidth per

channel ''',

5:'''Impact parameter = Ze^2 cot (0/2)/ 4 π ε0 (1⁄2

mv^2)''',

6:'''Energy equivalence relation E = mc^2''',
7:'''Binding Energy = ∆mc^2 ''',
8:'''Distance of closest approach = 1/2mv^2 = 1/4 π ε0

''',

9:'''Size of nucleus = R = Ro A^1/2''',
10:'''Mass Defect = ∆m[Zmp + (A-Z)mo]-M '''}

    print('='*125)
    for key, value in formulae.items():
        print(key, ' : ', value)
        print('='*125)

def Add_Task():
    import mysql.connector as sq
    conn=sq.connect(host='localhost',user='root',passwd='root',database='CS_Project')
    cur=conn.cursor()
    n=int(input('Enter serial number:'))
    t=input('Enter task:')
    d=input('Enter date:')
    qr="insert into ToDo_List(S_No, Task, Due_Date) values({}, '{}','{}')".format(n,t,d)
    cur.execute(qr)
    conn.commit()
    conn.close()

def Show_Tasks():
    import mysql.connector as sq
    conn=sq.connect(host='localhost',user='root',passwd='root',database='CS_Project')
    cur=conn.cursor()
    qr='select * from ToDo_List'
    cur.execute(qr)
    print('S_No',' '*5, 'Tasks', ' '*15, 'Due Date')
    data=cur.fetchall()
    for i in data:
        print('='*50)
        for j in i:
            print(j, end=' '*3)
            print()
            print()
            conn.commit()
            conn.close()

#main menu for students
def StuMain():
    print('='*125)
    ch='y'
    while ch=='y' or ch=='Y':
        print('1. Chapter Formulae \n2. Quizzes \n3. To Do List \n4. Progress \n5. Logout')
        n=int(input('Enter operation:'))
        if n==1:
            Formulae()
        elif n==2:
            Quizzes()
        elif n==3:
            Show_Tasks()
        elif n==4:
            n1=int(input('1.Progress Records \n2.Graphical Progress\n___'))

            if n1==1:
                StuProgress(Name)
            elif n1==2:
                GetScores(Name)
                StuMain()
        elif n==5:
            break
        else:
            print('No operation')
            ch=input('Would you like to try again? (y/n)')

#formulae function
def Formulae():
    print('='*125)
    print('Choose Chapter:')
    chapters = {1:'Chapter-1: Ray Optics', 2:'Chapter-2: Wave Optics',3:'Chapter-3: Semiconductor Electronics Materials, Devices And SimpleCircuits',4:'Chapter-4: Dual Nature of Radiation and Matter',5:'Chapter-5: Atoms', 6:'Chapter\-6: Nuclei'}
    for i in chapters:
        print(chapters[i])
    print('='*125)
    ch=int(input('Enter chapter: '))
    if ch==1:
        RayOpticsFormulae()
    elif ch==2:
        WaveOpticsFormulae()
    elif ch==3:
        SemiconductorsFormulae()
    elif ch==4:
        DualNatureFormulae()
    elif ch==5:
        AtomsFormulae()
    elif ch==6:
        NucleiFormulae()
    else:
        print('Invalid input')

#quiz function
def Quizzes():
    print('='*125)
    print('Choose chapter:')
    chapters = {1:'Chapter-1: Ray Optics', 2:'Chapter-2: Wave Optics',3:'Chapter-3: Semiconductor Electronics Materials, Devices And SimpleCircuits',4:'Chapter-4: Dual Nature of Radiation and Matter',5:'Chapter-5: Atoms', 6:'Chapter\-6: Nuclei'}
    for i in chapters:
        print(chapters[i])
    print('='*125)
    ch=int(input('Enter chapter: '))
    if ch==1:
        RayOpticsQuiz()
    elif ch==2:
        WaveOpticsQuiz()
    elif ch==3:
        SemiconductorsQuiz()
    elif ch==4:
        DualNatureQuiz()
    elif ch==5:
        AtomsQuiz()
    elif ch==6:
        NucleiQuiz()
    else:
        print('Invalid input')

#main menu for teachers
def TeaMain():
    print('='*125)
    ch='y'
    while ch=='Y' or ch=='y':
        print('''1. Add Student \n2. Student Details \n3. Assignments\n4. Logout''')
        n=int(input('Enter Operation:'))
        if n==1:
            name=input("Enter Student's Name:")
            ID=input('Create Student ID:')
            pin=int(input('Create Student Pincode:'))
            AddStu(name,ID,pin)
        elif n==2:
            StuDetails()
        elif n==3:
            n1=int(input('1. View Tasks \n2. Add Tasks \n-'))
            if n1==1:
                Show_Tasks()
            elif n1==2:
                Add_Task()
            else:
                print('Invalid Input')
        elif n==4:
            break
        else:
            print('No Operation.')
            ch==input('Would you like to try again? (y/n)')
print('='*125)
print(' '*50, 'WELCOME TO PHYSICS IS EZ')
print('='*125)
ch1=input('Are you already registered? \nType "y" to login or "n" to register \n-')
ch2=int(input('Are you a \n1.Student \n2.Teacher \n-'))
if ch1=='y':
    if ch2==1:
        name1=input('Enter name:')
        Name=''
        for i in name1.split():
            Name+=i
        StuLogin()
    elif ch2==2:
        TeaLogin()
    else:
        print('Invalid Input')
elif ch1=='n':
    if ch2==1:
        name1=input('Enter name:')
        Name=''
        for i in name1.split():
            Name+=i
        StuRegister()
    elif ch2==2:
        TeaRegister()
else:
    print('Invalid Input')