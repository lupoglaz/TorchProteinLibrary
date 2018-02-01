void Coords2RMSD_forward( THDoubleTensor *src, THDoubleTensor *dst, THDoubleTensor *rmsd, THDoubleTensor *ce_src, THDoubleTensor *ce_dst,THDoubleTensor *U_ce_src, THDoubleTensor *UT_ce_dst,THIntTensor *num_atoms);
void Coords2RMSD_backward(THDoubleTensor *grad_atoms, THDoubleTensor *grad_output,THDoubleTensor *ce_src, THDoubleTensor *ce_dst,THDoubleTensor *U_ce_src, THDoubleTensor *UT_ce_dst,THIntTensor *num_atoms);