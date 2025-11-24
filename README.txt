Napasorn(TK) Visuthiwat
CS480 Computer Graphics
PA2
10/14/2025

Collaborators: Daniel Scrivener

Resources Consulted:
- Course Lecture Notes

Summary
- Hierarchical BabyRobot: Tree-based hierarchy of component objects
- Components: more than 10 joints and limbs
- Parent-child Matrix propagation for realistic movement
- Mult-select System: selected_components set storing component references
    * 5 pre-defined poses: a - e keys
    * number 0 - 9 keys toggle compenent selection
- Axis Management: axisBucket array that stores [x,Y,Z]
- Apply Rotations to all selected Components simultaneously
- Five Test Poses : Running, Jumping, Standing, Balancing, and Dancing
- Error Handling: Component existence checking
    - bounds checking with len(self.components)
- For Multi-select, I started from single-select then extended to multi-select
- Using Python sets as a way to select and deselect components


