#ifndef Z_EN_BOOM_H
#define Z_EN_BOOM_H

#include "global.h"

struct EnBoom;

typedef void (*EnBoomActionFunc)(struct EnBoom*, GlobalContext*);

typedef struct EnBoom {
    /* 0x0000 */ Actor actor;
    /* 0x0144 */ char unk_144[0xAC];
    /* 0x01F0 */ EnBoomActionFunc actionFunc;
} EnBoom; // size = 0x1F4

extern const ActorInit En_Boom_InitVars;

#endif // Z_EN_BOOM_H
