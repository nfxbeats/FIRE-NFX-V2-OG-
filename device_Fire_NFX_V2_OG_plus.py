# name=FIRE-NFX-V2-OG+
# supportedDevices=FL STUDIO FIRE
#
# author: Nelson F. Fernandez Jr. <nfxbeats@gmail.com>
#

from fireNFX_Defs import *
from FIRE_NFX_OG_plus import * 
from FIRE_NFX_V2 import *

FireMode = 0 
_ShiftHeld = False
_AltHeld = False 

FireOG = TFire()
FireNFX = TFireNFX() 

Fire = FireNFX

def ToggleFireMode():
    global FireMode
    global Fire 

    if(FireMode == 0):
        print('changing to FIRE-OG+ mode')
        Fire = FireOG
        FireMode = 1
    else:
        print('changing to FIRE-NFX=V2 mode')
        Fire = FireNFX
        FireMode = 0 

def OnInit():
    Fire.OnInit()

def OnDeInit():
    Fire.OnDeInit()

def OnDisplayZone():
    Fire.OnDisplayZone()

def OnIdle():
    Fire.OnIdle()

def OnMidiIn(event):
    global _ShiftHeld
    global _AltHeld

    ctrlID = event.data1

    if(ctrlID == IDShift):
        _ShiftHeld = (event.data2 > 0)
    elif(ctrlID == IDAlt):
        _AltHeld = (event.data2 > 0)

    if(_AltHeld) and (IDRec == ctrlID and event.data2 == 0): # on release
        event.handled = True
        OnDeInit()
        ToggleFireMode()
        OnInit()
    else:
        Fire.OnMidiIn(event)

def OnMidiMsg(event):
    Fire.OnMidiMsg(event)

def OnRefresh(Flags):
    Fire.OnRefresh(Flags)

def OnUpdateLiveMode(LastTrackNum):
    Fire.OnUpdateLiveMode(1, LastTrackNum)

def OnUpdateBeatIndicator(Value):
    Fire.OnUpdateBeatIndicator(Value)

def OnProjectLoad(status):
    print('Project Loading...', status)
    Fire.OnProjectLoad(status)

def OnDoFullRefresh():
    Fire.OnDoFullRefresh()

def OnDirtyChannel(chan, flags):
    Fire.OnDirtyChannel(chan, flags)

def OnSendTempMsg(msg, duration):
    Fire.OnSendTempMsg(msg, duration)    

def OnNoteOn(event):
    Fire.OnNoteOn(event)

def OnNoteOff(event):
    Fire.OnNoteOff(event)

def OnSysEx(event):
    Fire.OnSysEx(event)

def OnControlChange(event):
    Fire.OnControlChange(event)

def OnProgramChange(event):
    Fire.OnProgramChange(event)

def OnPitchBend(event):
    Fire.OnPitchBend(event)

def OnKeyPressure(event):
    Fire.OnKeyPressure(event)

def OnChannelPressure(event):
    Fire.OnChannelPressure(event)

def OnMidiOutMsg(event):
    Fire.OnMidiOutMsg(event)

def OnDirtyMixerTrack(track):
    Fire.OnDirtyMixerTrack(track)

def OnFirstConnect():
    Fire.OnFirstConnect()

def OnWaitingForInput():
    Fire.OnWaitingForInput() 
