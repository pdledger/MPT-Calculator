from netgen.occ import *

def step_mesher(filename, output_filename='outputstepoutside.vol', add_boundary_layer=False, boundary_layer_mat_name='default'):
    # Loading in and healing step geometry
    geo = OCCGeometry(filename)
    geo.Heal()

    # Assigning material names and boundary conditions
    geo.shape.bc('default')
    geo.shape.mat('mat1')
    geo.shape.solids.name='mat1' # This sets the domain name. Does not have to match mat1 but is set to be the same for convience
    geo.shape.faces.name='default'

    # Creating boundary box
    bounding_box = Box(Pnt(-1000, -1000, -1000), Pnt(1000,1000,1000))
    bounding_box.mat('air')
    bounding_box.bc('outer')
    bounding_box.maxh = 200

    # Adding bounding box to original geometry
    geo2 = OCCGeometry(Glue([geo.shape, bounding_box]))

    # Meshing object
    mesh = geo2.GenerateMesh()

    if add_boundary_layer is True:
        if boundary_layer_mat_name == 'default':
            mat = 'mat1'
        else:
            mat = boundary_layer_mat_name

        #mesh.BoundaryLayer(boundary=".*", thickness=[1], material=mat,
        #                   domains='mat1', outside=False)
        mesh.BoundaryLayer(boundary=".*", thickness=[0.04], material=mat,
                           domains='mat1', outside=False)


    mesh.Save(output_filename)


if __name__ == '__main__':
    filename = r'bomblet_faceted_coarse.step'
    step_mesher(filename,add_boundary_layer=True)
#    step_mesher(filename,add_boundary_layer=True,boundary_layer_mat_name='copper') # allows the BoundaryLayer to have a different material name to
#    that of the solid (mat1 in this case) eg for coated objects with copper coating.
