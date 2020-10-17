# Col226

#Vectors and Matrics in Ocaml
The task is to model the data types of (a) vectors and (b) m x n matrices.

The basic types and type constructions you will use are OCaml floats and OCaml lists.

Vectors:

Define vectors as lists of floats.  Write efficient and documented programs to perform the following operations on vectors:

vdim: vector -> int,  returns the dimension of a given vector
mkzerov: int -> vector, given a dimension n > 0, returns the zero vector of that dimension
isvzerov: vector -> bool, checks if a given vector is a  zero vector
addv: vector -> vector -> vector,  adds two vectors v1 and v2 (of the same dimension)
scalarmultv: float -> vector -> vector,  given a scalar c and a vector v, performs the scalar multiplication 
dotprodv: vector -> vector -> float, given two vectors  v1 and v2 of the same dimension, returns their dot product v1 . v2
crossprodv: vector -> vector -> vector, given two vectors v1 and v2 in 3 dimensions, returns their cross product  v1 x v2.   (In general, for extra credit, you can define a function crossprodv of  n-1 vectors with dimension n).



Matrices:

Define matrices as lists of lists of floats (in row major form).  Write efficient and documented programs to perform the following operations on vectors:

mdim: matrix -> int * int,  returns the dimensions of a given matrix
mkzerom: int -> int -> matrix, given a dimension m, n > 0, returns the zero m x n matrix
iszerom: matrix -> bool, checks if a given matrix is a  zero matrix
mkunitm: int  -> matrix, given a dimension m > 0, returns the unit m x m (square) matrix
isunitm: matrix -> bool, checks if a given matrix is a unit (square) matrix
addm: matrix -> matrix -> matrix, adds two matrices m1 and m2 (of the same dimensions)
scalarmultm: float -> matrix -> matrix,  given a scalar c and a matrix m, performs the scalar multiplication 
multm: matrix -> matrix -> matrix, multiply two matrices m1 and m2 (assuming their dimensions allow them to be multiplied
transm: matrix -> matrix, transpose a given matrix
detm: matrix -> float, compute the determinant of a matrix (assuming it is a square matrix).
invm: matrix -> matrix, return the inverse of a given matrix (if defined).
