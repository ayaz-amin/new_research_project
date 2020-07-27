import torch
import torch.nn as nn

from type_model import TypeModel
from rendering_model import RenderingModel


class AttentionInduction(nn.Module):
    '''
    The full Attention Induced Program Learning model. The model
    consists of three sub-models:
        a) Type model
        b) Rendering model
        c) Deformation (token) model

    Parameters
    ----------

    max_k: int
        Maximum number of parts that can be present in an image at once
    num_parts: int
        Number of possible sub-parts that can be used to construct an image
    filter_size: (int, int)
        The shape of the convolution kernels for convolving over the sparse
        representation of an image
    image_shape: (int, int)
        The shape of the (generated) image  
    '''

    def __init__(self, max_k=5, num_parts=10, filter_size=(64, 64), image_shape=(105, 105)):
        super(AttentionInduction, self).__init__()
        '''
        Attributes
        ----------

        type_model: nn.Module
            The type model that generates, well, a type
        rendering_model: nn.Module
            The rendering model renders the final image
        token_model: nn.Module
            The token model generates slight deformations onto the final image
        '''

        self.type_model = TypeModel(max_k=max_k, num_parts=num_parts, image_shape=image_shape)
        self.rendering_model = RenderingModel(num_parts=num_parts, filter_size=filter_size, image_shape=image_shape)
        #TODO: implement token model. A Spatial Transformer will probably do
        self.token_model = TokenModel()