/*
 * File: z_en_talk.c
 * Overlay: ovl_En_Talk
 * Description: Green Target Spot (e.g., Indigo-Go's Poster)
 */

#include "z_en_talk.h"

#define FLAGS 0x00000009

#define THIS ((EnTalk*)thisx)

void EnTalk_Init(Actor* thisx, GlobalContext* globalCtx);
void EnTalk_Destroy(Actor* thisx, GlobalContext* globalCtx);
void EnTalk_Update(Actor* thisx, GlobalContext* globalCtx);

void func_80BDE058(EnTalk* this, GlobalContext* globalCtx);
void func_80BDE090(EnTalk* this, GlobalContext* globalCtx);

#if 0
const ActorInit En_Talk_InitVars = {
    ACTOR_EN_TALK,
    ACTORCAT_ITEMACTION,
    FLAGS,
    GAMEPLAY_KEEP,
    sizeof(EnTalk),
    (ActorFunc)EnTalk_Init,
    (ActorFunc)EnTalk_Destroy,
    (ActorFunc)EnTalk_Update,
    (ActorFunc)NULL,
};

#endif

#pragma GLOBAL_ASM("asm/non_matchings/overlays/ovl_En_Talk/EnTalk_Init.s")

#pragma GLOBAL_ASM("asm/non_matchings/overlays/ovl_En_Talk/EnTalk_Destroy.s")

#pragma GLOBAL_ASM("asm/non_matchings/overlays/ovl_En_Talk/func_80BDE058.s")

#pragma GLOBAL_ASM("asm/non_matchings/overlays/ovl_En_Talk/func_80BDE090.s")

#pragma GLOBAL_ASM("asm/non_matchings/overlays/ovl_En_Talk/EnTalk_Update.s")
