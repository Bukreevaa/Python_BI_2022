import numpy as np
if __name__ == "__main__":
   array1_tarrantion_movies = np.array(['Reservoir Dogs ', 'Pulp Fiction', 
'Jackie Brown', 'Kill Bill: Vol. 1', 'Kill Bill: Vol. 2', 'Death Proof', 
'Inglourious Basterds',  'Django Unchained', 'The Hateful Eight', 'Once 
Upon a Time in Hollywoo'])
   array2 = np.eye(5)
   array3 = np.linspace(0, 25, 300)



def matrix_multiplication(matrix1, matrix2):
    try:
        result = np.multiply(matrix1, matrix2)
        return result
    except ValueError:
        return print('does not satisfy the condition of matrix 
multiplication')

def multiplication_check(matrix_list):
  for i in range(len(matrix_list) - 1):
    if matrix_list[i].ndim != 2 or len(matrix_list) < 2:
      return False
      break
    if matrix_list[i+1].ndim != 2:
      return False
      break
    rows1, columns1 = matrix_list[i].shape
    rows2, columns2 = matrix_list[i+1].shape
    if columns1 == rows2:
      continue
    else:
      return False
      break
  return True

def multiply_matrices(matrix_list):
  if multiplication_check(matrix_list):
    result = np.multiply(matrix_list[0], matrix_list[1])
    for i in range(2, len(matrix_list) - 1):
      result = np.multiply(result, matrix_list[i])
  else:
    return None
  return (result)

def compute_2d_distance(point_one, point_two):
    square = np.square(point_one - point_two)
    sum_square = np.sum(square)
    distance = np.sqrt(sum_square)
    return distance

def compute_multidimensional_distance(point_one, point_two):
    square = np.square(point_one - point_two)
    sum_square = np.sum(square)
    distance = np.sqrt(sum_square)
    return distance

def compute_pair_distances(twodarray):
   return np.linalg.norm(array[:, None, :] - array[None, :, :], axis=-1)
