# Col226

# Vectors and Matrics in Ocaml
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

# Type Checker in Prolog
need to write a Prolog predicate hastype(Gamma, E, T), where 



Gamma is a list of variable-type pairs, representing type assumptions on variables
E is an object language expression, 
T is a type.


This predicate is mutually recursively defined with another Prolog predicate

 typeElaborates(Gamma, D, Gamma')

where D is a definition.



E ranges over (at least)



variables, modelled as say variable(X)
constants, both numerical and boolean (at least)
arithmetic operations over numerical expressions
boolean operations over boolean expressions
comparison operations over numerical expressions
equality over arbitrary expressions, where equality can be decided
conditional expressions if_then_else
qualified expressions of the form let D in E end
function abstractions \X.E  with functions as first-class citizens
function application (E1 E2)  
n-tuples  (n >= 0)
expressions using projection operations.
....possible extensions to constructors, and case analysis expressions


and 

D ranges over (at least)



simple definitions X =def= E
sequential definitions D1; D2
parallel definitions D1 || D2
local definitions local D1 in D2 end
... possible extension to recursive definitions
and 

T ranges over (at least)





Type variables modelled as say TypeVar(A) 
Base types tint, tbool, ...
Arrow types T1 -> T2 |
cartesian product types T1 * ... * Tn  (n>1)

# Signatures, Terms, substitutions, unifiers
type term = V of variable | Node of symbol * (term list);;

Choose suitable type representations for types variable and symbol.



Given a signature consisting of symbols and their arities (>= 0) in any suitable form -- either as a list of (symbol, arity) pairs, or as a function from symbols to arities, write a function check_sig that checks whether the signature is a valid signature (no repeated symbols, arities are non-negative etc.)
Given a valid signature (checked using check_sig), define a function wfterm that checks that a given preterm is well-formed according to the signature.
Define functions ht, size and vars that given a well-formed term, return its height, its size and the set (represented as a list with no duplicates) of variables appearing in it respectively.  Use map, foldl and other such functions as far as possible wherever you use lists.  
Define a suitable representation for substitutions.  Come up with an efficient representation of composition of substitutions. 
Define the function subst that given a term t and a substitution s, applies the (Unique Homomorphic Extension of) s to t.  Ensure that subst is efficiently implemented. 
Define the function mgu that given two terms t1 and t2, returns their most general unifier, if it exists and otherwise raises an exception NOT_UNIFIABLE.


