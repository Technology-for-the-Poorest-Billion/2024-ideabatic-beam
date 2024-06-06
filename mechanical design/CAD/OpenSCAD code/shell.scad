// bottom case (purple)
translate([-212,-176.5,-130]){
    color(c=[0.3,0,0.3,1]){
        import("/Users/vanessalam/Desktop/Hex case V2-1.STEP.STL");
        }
    }
 
// top case (blue)
rotate([0, 180,0]){   
    translate([-212,-176.5,-130]){
        color(c=[0,0.3,0.5,1]){
            import("/Users/vanessalam/Desktop/Hex case V2-1.STEP.STL");
        }
        }
    }

// bottom chassis (green)
rotate([90, 180,0]){
    translate([-131,-2,-195]){
        color(c=[0,0.5,0.3,1]){
            import("/Users/vanessalam/Desktop/Chassis S V2-1.STEP.STL");
            }
        }
    }
 
// top chassis (yellow)
rotate([90, 0,0]){
    translate([-131,-2,-195]){
        import("/Users/vanessalam/Desktop/Chassis S V2-1.STEP.STL");
        }
    }
    
