/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | www.openfoam.com
     \\/     M anipulation  |
-------------------------------------------------------------------------------
    Copyright (C) YEAR AUTHOR, AFFILIATION
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.

Description
    Template for use with codeStream.

\*---------------------------------------------------------------------------*/

#include "dictionary.H"
#include "Ostream.H"
#include "Pstream.H"
#include "pointField.H"
#include "tensor.H"
#include "unitConversion.H"

//{{{ begin codeInclude
#line 47 "/home/romanovadi/cases/OpenFOAM/flowPastCylinder/WALE_noWallFunctions/3D/Re10000_nz20_nRadial100_m.._Cd.._Clp.._yPlus../system/blockMeshDict.#codeStream"
#include "pointField.H"
//}}} end codeInclude

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode


// * * * * * * * * * * * * * * * Global Functions  * * * * * * * * * * * * * //

extern "C" void codeStream_7168fc8ee90442ce033d55f2e04d9a7dc6810e2c(Foam::Ostream& os, const Foam::dictionary& dict)
{
//{{{ begin code
    #line 52 "/home/romanovadi/cases/OpenFOAM/flowPastCylinder/WALE_noWallFunctions/3D/Re10000_nz20_nRadial100_m.._Cd.._Clp.._yPlus../system/blockMeshDict.#codeStream"
pointField points
        ({
            /* 0*/ { 0.50000000, 0, -0.50000000 },
            /* 1*/ { 5.50000000, 0, -0.50000000 },
            /* 2*/ { 65.50000000, 0, -0.50000000 },
            /* 3*/ { 65.50000000, 3.88908729, -0.50000000 },
            /* 4*/ { 3.88908729, 3.88908729, -0.50000000 },
            /* 5*/ { 0.35355339, 0.35355339, -0.50000000 },
            /* 6*/ { 65.50000000, 15.50000000, -0.50000000 },
            /* 7*/ { 3.88908729, 15.50000000, -0.50000000 },
            /* 8*/ { 0, 15.50000000, -0.50000000 },
            /* 9*/ { 0, 5.50000000, -0.50000000 },
            /*10*/ { 0, 0.50000000, -0.50000000 },
            /*11*/ { -0.50000000, 0, -0.50000000 },
            /*12*/ { -5.50000000, 0, -0.50000000 },
            /*13*/ { -15.50000000, 0, -0.50000000 },
            /*14*/ { -15.50000000, 3.88908729, -0.50000000 },
            /*15*/ { -3.88908729, 3.88908729, -0.50000000 },
            /*16*/ { -0.35355339, 0.35355339, -0.50000000 },
            /*17*/ { -15.50000000, 15.50000000, -0.50000000 },
            /*18*/ { -3.88908729, 15.50000000, -0.50000000 }
        });

        // Duplicate z points for zmax
        const label sz = points.size();
        points.resize(2*sz);
        for (label i = 0; i < sz; ++i)
        {
            const point& pt = points[i];
            points[i + sz] = point(pt.x(), pt.y(), 0.50000000);
        }

        os  << points;
//}}} end code
}


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

} // End namespace Foam

// ************************************************************************* //

