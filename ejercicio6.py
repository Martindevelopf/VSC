"""6. Considere el siguiente programa:
 program Pr3Ej6;
 var x, y, z : Integer;
 begin
 x := 10;
 y := 11;
 z := 12;
 if (x > y) or (z > y) then
 if x > z then
 if y > z then
 writeln ('Termine.')
 else writeln ('No termino aun.')
 else writeln ('Nunca llega aqui.')
 end.
 (a) Indique qu´ e se exhibir´ a en la salida est´andar al ejecutarlo. Despu´es, ejec´utelo en m´aqui
na y compare lo que esperaba con la salida que se exhibe.
 (b) Reescriba el programa anterior con una indentaci´ on adecuada.
 (c) Asumiendo que las expresiones booleanas se eval´uan por circuito corto, diga si la
 expresi´ on z > y es evaluada."""

x = 10
y = 11
z = 12

if x>y or z>y:
    if x> z:
        if y>z:
            print("termine")
else:
    print("no termine aun")
    