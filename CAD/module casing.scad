//casing bottom
difference() {
    cube([22,54,6], true);   
    
    translate([0,0,0.5]) {
        cube([21.5,53.5,6], true);
        }
    }
    
//connections to pico
translate([-6,-24,-1]){
    cylinder(h = 4, r=1, center = true);
    } 
    
translate([6,-24,-1]){
    cylinder(h = 4, r=1, center = true);
    } 
    
translate([6,24,-1]){
    cylinder(h = 4, r=1, center = true);
    } 
    
translate([-6,24,-1]){
    cylinder(h = 4, r=1, center = true);
    } 
    
 
