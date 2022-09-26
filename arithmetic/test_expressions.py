text_expressions = (
    '2+3/4', '(91)', '6*3+14+0', '6+8', '(8-34*8-3)', '13+15-1', '(3*16+3*1)', '6*8', '(6+16)/16', '6*55',
    '76+18+4-(98)-7/15', '(0*32)', '(4*34)+34', '8+3+2', '6+8', '(6*16)+16', '2-3/6', '2*3', '(36+8-9)', '0/8/6',
    '6*8+7', '(((89)))', '1+33', '(12+3-5)', '(78)-(7/56*33)', '(((73)))', '2+3', '19*(8+8)', '50+0/1', '2+77',
    '6-3*14*0', '(8*34+8*3)', '(8*10)', '78/8-9', '6+8', '(78)/(7+56-33)', '2*3-6', '(((73)))', '(5-12+16)',
    '(9-36+34)', '2*3', '0-4+7/3', '2*77', '(59)', '((8))', '3-30/(8*39)', '(-3)+5', '(55)/(54)-55*92/13/((36))',
    '86*84*87+(96/46)+59', '54*30*7/(10)/5+39', '((((71))))*((74))', '(((89)))', '((((49))))*((46))', '(5*12/16)',
    '(12*3/5)', '(4-0+4)', '(91)', '3+88', '1/33', '(9*36/34)', '2+3', '(((58)))', '19+(8/8)', '(((58)))', '(68)',
    '(23)', '2*3+4', '76*18*4/(98)/7+15', '0+8+6', '((((71))))+((74))', '3/88', '6*8', '(55)-(54)*55+92-13-((36))',
    '(68)', '(99)-(97)*99+16-38-((84))', '1-18/(3*15)', '(99)/(97)-99*16/38/((84))', '((3))', '54+30+7-(10)-5/39',
    '38*39/3', '(50)/(5+94-88)', '(8-10)', '6*8', '2*3', '(81)-18*(((8))*59-14)', '1/18+(3-15)', '((3))', '31*(0+0)',
    '((8))', '0*4/7-3', '4*8+37+2', '8-6+4/1', '(50)-(5/94*88)', '((((49))))+((46))', '13*15/1', '3/30+(8-39)',
    '4-8*37*2', '8/3/2', '(59)', '(-8)+9', '(0-32)', '(23)', '(4+34)/34', '2+3', '78+8/9', '(7-2+7)', '(36*8/9)',
    '38+39-3', '6+8/7', '6+55', '8*6/4-1', '(81)/18-(((8))-59/14)', '6*8-4', '(3-16*3-1)', '6-8/4', '(4*0/4)',
    '(7*2/7)', '86+84+87/(96-46)/59', '-6')
expressions_incorrect_python = {'(9-09)*09': '(9-9)*9', '07-(4*4)': '7-(4*4)', '0-04/(6*03)': '0-4/(6*3)',
    '(3*05/09)': '(3*5/9)', '9*6+01+2': '9*6+1+2', '9+6-01-2': '9+6-1-2', '(6+09-6+0)': '(6+9-6+0)',
    '07+(4/4)': '7+(4/4)', '(40)-04*(((4))*37-01)': '(40)-4*(((4))*37-1)',
    '(40)/04+(((4))+37/01)': '(40)/4+(((4))+37/1)', '(33)/(31)+33-75/06/((69))': '(33)/(31)+33-75/6/((69))',
    '(05-6/3)': '(5-6/3)', '89+04+1-(74)-8/03': '89+4+1-(74)-8/3', '0/04*(6+03)': '0/4*(6+3)', '(4*02)': '(4*2)',
    '(05+6-3)': '(5+6-3)', '(4+02)': '(4+2)', '(6*09+6*0)': '(6*9+6*0)', '06+03-0': '6+3-0',
    '89-04-1/(74)/8*03': '89-4-1/(74)/8*3', '(3+05*09)': '(3+5*9)', '(9+09)/09': '(9+9)/9',
    '(33)-(31)*33+75-06-((69))': '(33)-(31)*33+75-6-((69))'}

incorrect_expressions = ['5 +/ 6+ 8', '5//6', '6+++1', '--6+3', '5(43+79)*05-79', '-+5+8', '', '()', '-abs ', '6---1',
                         '(6)(5)', '/66', '(6)+5)']
