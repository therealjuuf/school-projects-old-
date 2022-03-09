function varargout = gui(varargin)
% GUI MATLAB code for gui.fig
%      GUI, by itself, creates a new GUI or raises the existing
%      singleton*.
%
%      H = GUI returns the handle to a new GUI or the handle to
%      the existing singleton*.
%
%      GUI('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in GUI.M with the given input arguments.
%
%      GUI('Property','Value',...) creates a new GUI or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before gui_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to gui_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help gui

% Last Modified by GUIDE v2.5 21-Jan-2019 10:46:42

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @gui_OpeningFcn, ...
                   'gui_OutputFcn',  @gui_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before gui is made visible.
function gui_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to gui (see VARARGIN)

% Choose default command line output for gui
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);


% UIWAIT makes gui wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = gui_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --------------------------------------------------------------------
function Open_Callback(hObject, eventdata, handles)
% hObject    handle to Open (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

global filename;
global previousImage;
[filename,filepath]=uigetfile({'*.*'},'Select and image');
global selectedImage; 
global currentImage;
global bright_old;
global appliedImage;
bright_old=0;
selectedImage = imread(strcat(filepath, filename));
currentImage=selectedImage;
previousImage=selectedImage;
appliedImage=previousImage;
axes(handles.ori_img);
imshow(currentImage);
RenderCurrent(handles,currentImage);
Apply(handles);
zoom on;

% --------------------------------------------------------------------
function Save_Callback(hObject, eventdata, handles)
% hObject    handle to Save (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global filename;
global appliedImage;
imwrite(appliedImage,filename);


% --------------------------------------------------------------------
function SaveAs_Callback(hObject, eventdata, handles)
% hObject    handle to SaveAs (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
imsave(handles.applied_img);

% --------------------------------------------------------------------
function Exit_Callback(hObject, eventdata, handles)
% hObject    handle to Exit (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
close all force;


function rotate_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double
global rotato;
global currentImage;

%appliedImage=currentImage;
%
%cla(handles.applied_img);
%axesHandlesToChildObjects = findobj(handles.applied_img, 'Type', 'image');
%if ~isempty(axesHandlesToChildObjects)
%  delete(axesHandlesToChildObjects);
%end
%axes(handles.applied_img);
%imshow(appliedImage);
%
%
rot=str2double(get(hObject,'String'));
rotato=0+rotato;
currentImage=imrotate(currentImage,rot);
%
%cla(handles.current_img);
axesHandlesToChildObjects = findobj(handles.current_img, 'Type', 'image');
if ~isempty(axesHandlesToChildObjects)
  delete(axesHandlesToChildObjects);
end
RenderCurrent(handles,currentImage)


% --- Executes during object creation, after setting all properties.
function rotate_CreateFcn(hObject, eventdata, handles)
% hObject    handle to rotate (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function resize_x_Callback(hObject, eventdata, handles)
% hObject    handle to resize_x (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of resize_x as text
%        str2double(get(hObject,'String')) returns contents of resize_x as a double
global resize_x;
resize_x=str2double(get(hObject,'String'));

% --- Executes during object creation, after setting all properties.
function resize_x_CreateFcn(hObject, eventdata, handles)
% hObject    handle to resize_x (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function resize_y_Callback(hObject, eventdata, handles)
% hObject    handle to resize_y (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of resize_y as text
%        str2double(get(hObject,'String')) returns contents of resize_y as a double
global resize_y;
resize_y=str2double(get(hObject,'String'));

% --- Executes during object creation, after setting all properties.
function resize_y_CreateFcn(hObject, eventdata, handles)
% hObject    handle to resize_y (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in resize.
function resize_Callback(hObject, eventdata, handles)
% hObject    handle to resize (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global currentImage;
global appliedImage;
global resize_x;
global resize_y;
%appliedImage=currentImage;
%
%cla(handles.applied_img);
%axesHandlesToChildObjects = findobj(handles.applied_img, 'Type', 'image');
%if ~isempty(axesHandlesToChildObjects)
%  delete(axesHandlesToChildObjects);
%end
%axes(handles.applied_img);
%imshow(appliedImage);
%
currentImage=imresize(currentImage,[resize_x,resize_y]);
%
%cla(handles.current_img);
axesHandlesToChildObjects = findobj(handles.current_img, 'Type', 'image');
if ~isempty(axesHandlesToChildObjects)
  delete(axesHandlesToChildObjects);
end
RenderCurrent(handles,currentImage)


% --- Executes on button press in Apply.
function Apply_Callback(hObject, eventdata, handles)
% hObject    handle to Apply (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global appliedImage;
Apply(handles);

function Apply(handles)
global currentImage;
global previousImage;
global appliedImage;
previousImage=appliedImage;
currentImage=getimage(handles.current_img);
appliedImage=currentImage;

%cla(handles.applied_img);
axesHandlesToChildObjects = findobj(handles.applied_img, 'Type', 'image');
if ~isempty(axesHandlesToChildObjects)
 delete(axesHandlesToChildObjects);
end

axes(handles.applied_img)
imshow(currentImage);

RenderCurrent(handles,currentImage)


function RenderCurrent(handles,image)
axesHandlesToChildObjects = findobj(handles.current_img, 'Type', 'image');
if ~isempty(axesHandlesToChildObjects)
 delete(axesHandlesToChildObjects);
end
axes(handles.current_img);
imshow(image);
renderSpectrum(handles);
axes(handles.HistogramAxes)

imhist(image);


% --- Executes on button press in previous.
function previous_Callback(hObject, eventdata, handles)
% hObject    handle to previous (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
PreviousApply(handles);

function PreviousApply(handles)
global currentImage;
global appliedImage;
global previousImage;
%previousImage=appliedImage;
%appliedImage=currentImage;
appliedImage=previousImage;
%currentImage=previousImage;
%cla(handles.applied_img);
axesHandlesToChildObjects = findobj(handles.applied_img, 'Type', 'image');
if ~isempty(axesHandlesToChildObjects)
 delete(axesHandlesToChildObjects);
end
axesHandlesToChildObjects = findobj(handles.current_img, 'Type', 'image');
if ~isempty(axesHandlesToChildObjects)
 delete(axesHandlesToChildObjects);
end

axes(handles.applied_img)
imshow(appliedImage);

RenderCurrent(handles,appliedImage);


% --- Executes on slider movement.
function slider3_Callback(hObject, eventdata, handles)
% hObject    handle to slider3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
global currentImage;
global appliedImage;
global current_gecici;

axesHandlesToChildObjects = findobj(handles.current_img, 'Type', 'image');
if ~isempty(axesHandlesToChildObjects)
 delete(axesHandlesToChildObjects);
end

brightness=get(hObject,'Value');
current_gecici=currentImage+brightness;
RenderCurrent(handles,current_gecici)

% --- Executes during object creation, after setting all properties.
function slider3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to slider3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


% --- Executes on button press in restore.
function restore_Callback(hObject, eventdata, handles)
% hObject    handle to restore (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global currentImage;
global appliedImage;
global selectedImage;
appliedImage=selectedImage;

%cla(handles.applied_img);
axesHandlesToChildObjects = findobj(handles.applied_img, 'Type', 'image');
if ~isempty(axesHandlesToChildObjects)
 delete(axesHandlesToChildObjects);
end

axes(handles.applied_img)
imshow(appliedImage);

RenderCurrent(handles,currentImage)


% --- Executes on selection change in noisebox.
function noisebox_Callback(hObject, eventdata, handles)
% hObject    handle to noisebox (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns noisebox contents as cell array
%        contents{get(hObject,'Value')} returns selected item from noisebox
ApplyNoise(handles);

function ApplyNoise(handles)
global currentImage;
currentImage2=currentImage;
noise_var1 = str2double(get(handles.noisemean,'String'));
noise_var2 = str2double(get(handles.noisevar,'String'));
switch get(handles.noisebox,'Value')
    case 1
        textLabel = sprintf('Mean');
        set(handles.var1, 'String', textLabel);
        textLabel = sprintf('Variance');
        set(handles.var2, 'String', textLabel);
        if (~isnan(noise_var1)&&~isnan(noise_var2))
            currentImage2=imnoise(currentImage,'gaussian',noise_var1,noise_var2);
        elseif (~isnan(noise_var1)&&isnan(noise_var2))
            currentImage2=imnoise(currentImage,'gaussian',noise_var1);
        elseif (isnan(noise_var1)&&isnan(noise_var2))
            currentImage2=imnoise(currentImage,'gaussian');
        end
  
    case 2
        textLabel = sprintf('Mean');
        set(handles.var1, 'String', textLabel);
        textLabel = sprintf('Variance');
        set(handles.var2, 'String', textLabel);
         if (~isnan(noise_var1)&&~isnan(noise_var2))
            currentImage2=imnoise(currentImage,'localvar',noise_var1,noise_var2);
         elseif (isnan(noise_var1)&&~isnan(noise_var2))
             currentImage2=imnoise(currentImage,'localvar',noise_var2);
         end
    case 3
        textLabel = sprintf('Not Used');
        set(handles.var1, 'String', textLabel);
        textLabel = sprintf('Not Used');
        set(handles.var2, 'String', textLabel);
        currentImage2=imnoise(currentImage,'poisson');
    case 4
        textLabel = sprintf('Noise Density');
        set(handles.var1, 'String', textLabel);
        textLabel = sprintf('Not Used');
        set(handles.var2, 'String', textLabel);
        if (isnan(noise_var1)&&~isnan(noise_var2))
            currentImage2=imnoise(currentImage,'salt & pepper',noise_var1);
        elseif (isnan(noise_var1)&&isnan(noise_var2))
            currentImage2=imnoise(currentImage,'salt & pepper');
        end
    case 5
        textLabel = sprintf('Variance');
        set(handles.var1, 'String', textLabel);
        textLabel = sprintf('Not Used');
        set(handles.var2, 'String', textLabel);
        if (isnan(noise_var1)&&~isnan(noise_var2))
            currentImage2=imnoise(currentImage,'speckle',noise_var1);
        elseif (isnan(noise_var1)&&isnan(noise_var2))
            currentImage2=imnoise(currentImage,'speckle');
        end
end

RenderCurrent(handles,currentImage2);

% --- Executes during object creation, after setting all properties.
function noisebox_CreateFcn(hObject, eventdata, handles)
% hObject    handle to noisebox (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function noisemean_Callback(hObject, eventdata, handles)
% hObject    handle to noisemean (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of noisemean as text
%        str2double(get(hObject,'String')) returns contents of noisemean as a double
ApplyNoise(handles);

% --- Executes during object creation, after setting all properties.
function noisemean_CreateFcn(hObject, eventdata, handles)
% hObject    handle to noisemean (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function noisevar_Callback(hObject, eventdata, handles)
% hObject    handle to noisevar (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of noisevar as text
%        str2double(get(hObject,'String')) returns contents of noisevar as a double
ApplyNoise(handles);

% --- Executes during object creation, after setting all properties.
function noisevar_CreateFcn(hObject, eventdata, handles)
% hObject    handle to noisevar (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in ApplyNoise.
function ApplyNoise_Callback(hObject, eventdata, handles)
% hObject    handle to ApplyNoise (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on selection change in noiseremovalbox.
function noiseremovalbox_Callback(hObject, eventdata, handles)
% hObject    handle to noiseremovalbox (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns noiseremovalbox contents as cell array
%        contents{get(hObject,'Value')} returns selected item from noiseremovalbox
ApplyNoiseRemove(handles);


function ApplyNoiseRemove(handles)
global currentImage;
currentImage2=currentImage;
noiseremoval_var1 = str2double(get(handles.noisevar1,'String'));
noiseremoval_var2 = str2double(get(handles.noisevar2,'String'));
switch get(handles.noiseremovalbox,'Value')
    case 1
        if (~isnan(noiseremoval_var1)&&~isnan(noiseremoval_var2))
            currentImage2=rgb2gray(currentImage);
            %currentImage2=medfilt2(currentImage,[filter_var1 filter_var2]);
            currentImage2=medfilt2(currentImage2,[noiseremoval_var1 noiseremoval_var2]);
        else
           currentImage2=rgb2gray(currentImage);
           currentImage2=medfilt2(currentImage2);
           %currentImage2=medfilt2(currentImage);
        end
  
    case 2
        textLabel = sprintf('Dimension M');
        set(handles.var1, 'String', textLabel);
        textLabel = sprintf('Dimension N');
        set(handles.var2, 'String', textLabel);
         if (~isnan(noiseremoval_var1)&&~isnan(noiseremoval_var2))
             currentImage2=rgb2gray(currentImage);
             %J = imnoise(currentImage2,'gaussian');
            currentImage2=wiener2(currentImage2,[noiseremoval_var1 noiseremoval_var2]);
            %currentImage2=currentImage2+60;
         else
             currentImage2=rgb2gray(currentImage);
             %J = imnoise(currentImage2,'gaussian');
             currentImage2=wiener2(currentImage2);
            % currentImage2=imrotate(currentImage2,90);
         end
       
    
end

RenderCurrent(handles,currentImage2); 

% --- Executes during object creation, after setting all properties.
function noiseremovalbox_CreateFcn(hObject, eventdata, handles)
% hObject    handle to noiseremovalbox (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function noisevar1_Callback(hObject, eventdata, handles)
% hObject    handle to noisevar1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of noisevar1 as text
%        str2double(get(hObject,'String')) returns contents of noisevar1 as a double


% --- Executes during object creation, after setting all properties.
function noisevar1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to noisevar1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function noisevar2_Callback(hObject, eventdata, handles)
% hObject    handle to noisevar2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of noisevar2 as text
%        str2double(get(hObject,'String')) returns contents of noisevar2 as a double


% --- Executes during object creation, after setting all properties.
function noisevar2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to noisevar2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton7.
function pushbutton7_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on selection change in EdgeBox.
function EdgeBox_Callback(hObject, eventdata, handles)
% hObject    handle to EdgeBox (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns EdgeBox contents as cell array
%        contents{get(hObject,'Value')} returns selected item from EdgeBox
ApplyEdge(handles);

function ApplyEdge(handles)
global currentImage;
%currentImage2=currentImage;
edge_var1 = str2double(get(handles.edgevar1,'String'));
edge_var2 = str2double(get(handles.edgevar2,'String'));
currentImage2=rgb2gray(currentImage);
switch get(handles.EdgeBox,'Value')
    case 1
        textLabel = sprintf('horizontal or vertical');
        set(handles.edgetext2, 'String', textLabel);
        if (~isnan(edge_var1)&&~isnan(edge_var2))
           edge_var2 = get(handles.edgevar2,'String');
            currentImage2=edge(currentImage2,'Sobel',edge_var1,edge_var2);
        elseif(~isnan(edge_var1)&&isnan(edge_var2))
           currentImage2=edge(currentImage2,'Sobel',edge_var1);
        else
            currentImage2=edge(currentImage2,'Sobel');
        end
  
    case 2
        textLabel = sprintf('horizontal or vertical');
        set(handles.edgetext2, 'String', textLabel);
        if (~isnan(edge_var1)&&~isnan(edge_var2))
            edge_var2 = get(handles.edgevar2,'String');
            currentImage2=edge(currentImage2,'Prewitt',edge_var1,edge_var2);
        elseif(~isnan(edge_var1)&&isnan(edge_var2))
           currentImage2=edge(currentImage2,'Prewitt',edge_var1);
        else
            currentImage2=edge(currentImage2,'Prewitt');
        end
      case 3
        textLabel = sprintf('horizontal or vertical');
        set(handles.edgetext2, 'String', textLabel);
        if (~isnan(edge_var1)&&~isnan(edge_var2))
            edge_var2 = get(handles.edgevar2,'String');
            currentImage2=edge(currentImage2,'Roberts',edge_var1,edge_var2);
        elseif(~isnan(edge_var1)&&isnan(edge_var2))
           currentImage2=edge(currentImage2,'Roberts',edge_var1);
        else
            currentImage2=edge(currentImage2,'Roberts');
        end
       case 4
        textLabel = sprintf('Standard Deviation');
        set(handles.edgetext2, 'String', textLabel);
        if (~isnan(edge_var1)&&~isnan(edge_var2))
            currentImage2=edge(currentImage2,'log',edge_var1,edge_var2);
        elseif(~isnan(edge_var1)&&isnan(edge_var2))
           currentImage2=edge(currentImage2,'log',edge_var1);
        else
            currentImage2=edge(currentImage2,'log');
       end  
       case 5
        textLabel = sprintf('Standard Deviation');
        set(handles.edgetext2, 'String', textLabel);   
        if (~isnan(edge_var1)&&~isnan(edge_var2))
            currentImage2=edge(currentImage2,'Canny',edge_var1,edge_var2);
        elseif(~isnan(edge_var1)&&isnan(edge_var2))
           currentImage2=edge(currentImage2,'Canny',edge_var1);
        else
            currentImage2=edge(currentImage2,'Canny');
       end         
       case 6
        textLabel = sprintf('Not Used');
        set(handles.edgetext2, 'String', textLabel);
        if (~isnan(edge_var1)&&~isnan(edge_var2))
            currentImage2=edge(currentImage2,'zerocross',edge_var1,edge_var2);
        elseif(~isnan(edge_var1)&&isnan(edge_var2))
           currentImage2=edge(currentImage2,'zerocross',edge_var1);
        else
            currentImage2=edge(currentImage2,'zerocross');
       end     
end

RenderCurrent(handles,currentImage2); 














% --- Executes during object creation, after setting all properties.
function EdgeBox_CreateFcn(hObject, eventdata, handles)
% hObject    handle to EdgeBox (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edgevar1_Callback(hObject, eventdata, handles)
% hObject    handle to edgevar1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edgevar1 as text
%        str2double(get(hObject,'String')) returns contents of edgevar1 as a double


% --- Executes during object creation, after setting all properties.
function edgevar1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edgevar1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edgevar2_Callback(hObject, eventdata, handles)
% hObject    handle to edgevar2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edgevar2 as text
%        str2double(get(hObject,'String')) returns contents of edgevar2 as a double


% --- Executes during object creation, after setting all properties.
function edgevar2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edgevar2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton8.
function pushbutton8_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton8 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on selection change in noiseremovalbox.
function FilterBox_Callback(hObject, eventdata, handles)
% hObject    handle to noiseremovalbox (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns noiseremovalbox contents as cell array
%        contents{get(hObject,'Value')} returns selected item from noiseremovalbox
ApplyFilter(handles)


function ApplyFilter(handles)
global currentImage;
%currentImage2=currentImage;
edge_var1 = str2double(get(handles.filtervar1,'String'));
edge_var2 = str2double(get(handles.filtervar2,'String'));
currentImage2=rgb2gray(currentImage);
textLabel = sprintf('Variable 2');
set(handles.filtertext2, 'String', textLabel);
textLabel = sprintf('Variable 1');
set(handles.filtertext1, 'String', textLabel);
switch get(handles.FilterBox,'Value')
    case 1
        textLabel = sprintf('Not Used');
        set(handles.filtertext2, 'String', textLabel);
        if (isnan(edge_var1)&&isnan(edge_var2))
           filter=fspecial('average');           
        else
             filter=fspecial('average',edge_var1);           
        end
    case 2
        textLabel = sprintf('Not Used');
        set(handles.filtertext2, 'String', textLabel);
        if (isnan(edge_var1)&&isnan(edge_var2))
           filter=fspecial('disk');           
        else
           filter=fspecial('disk',edge_var1);           
        end
    case 3
        textLabel = sprintf('Not Used');
        set(handles.filtertext2, 'String', textLabel);
        if (isnan(edge_var1)&&isnan(edge_var2))
           filter=fspecial('gaussian');           
        elseif(~isnan(edge_var1)&&~isnan(edge_var2))
           filter=fspecial('gaussian',edge_var1,edge_var2);           
        end
    case 4
        textLabel = sprintf('Not Used');
        set(handles.filtertext2, 'String', textLabel);
        if (isnan(edge_var1)&&isnan(edge_var2))
           filter=fspecial('laplacian');           
        else
           filter=fspecial('laplacian',edge_var1);           
        end   
    case 5
        if (isnan(edge_var1)&&isnan(edge_var2))
           filter=fspecial('log');           
        elseif(~isnan(edge_var1)&&~isnan(edge_var2))
           filter=fspecial('log',edge_var1,edge_var2);           
        end
    case 6
        if (isnan(edge_var1)&&isnan(edge_var2))
           filter=fspecial('motion');           
        elseif(~isnan(edge_var1)&&~isnan(edge_var2))
           filter=fspecial('motion',edge_var1,edge_var2);           
        end
    case 7
        textLabel = sprintf('Not Used');
        set(handles.filtertext2, 'String', textLabel);
        textLabel = sprintf('Not Used');
        set(handles.filtertext1, 'String', textLabel);
           filter=fspecial('prewitt');                    
    case 8
        textLabel = sprintf('Not Used');
        set(handles.filtertext2, 'String', textLabel);
        textLabel = sprintf('Not Used');
        set(handles.filtertext1, 'String', textLabel);
           filter=fspecial('sobel');                      
        
end
currentImage2=imfilter(currentImage2,filter,'replicate');
RenderCurrent(handles,currentImage2); 



function filtervar1_Callback(hObject, eventdata, handles)
% hObject    handle to filtervar1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of filtervar1 as text
%        str2double(get(hObject,'String')) returns contents of filtervar1 as a double


% --- Executes during object creation, after setting all properties.
function filtervar1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to filtervar1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function filtervar2_Callback(hObject, eventdata, handles)
% hObject    handle to filtervar2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of filtervar2 as text
%        str2double(get(hObject,'String')) returns contents of filtervar2 as a double


% --- Executes during object creation, after setting all properties.
function filtervar2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to filtervar2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function FilterBox_CreateFcn(hObject, eventdata, handles)
% hObject    handle to filterbox (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in LoadCustomFilter.
function LoadCustomFilter_Callback(hObject, eventdata, handles)
% hObject    handle to LoadCustomFilter (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global currentImage;
%currentImage2=currentImage;
currentImage2=rgb2gray(currentImage);
[filename1,filepath1]=uigetfile({'*.txt','.txt'},...
  'Select Your Filter');
  cd(filepath1);
filter = dlmread(filename1);
currentImage2=imfilter(currentImage2,filter,'replicate');
RenderCurrent(handles,currentImage2); 


% --- Executes on button press in getSpectrum.
function getSpectrum_Callback(hObject, eventdata, handles)
% hObject    handle to getSpectrum (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

%currentImage2=currentImage;

renderSpectrum(handles);





function renderSpectrum(handles)
crntI=getimage(handles.current_img);
if(size(crntI,3)==3)
    grayImage=rgb2gray(crntI);
else
    grayImage=crntI;
end
F=fft2(grayImage);
S=fftshift(log(1+abs(F)));
axesHandlesToChildObjects = findobj(handles.ImageSpectrum, 'Type', 'image');
if ~isempty(axesHandlesToChildObjects)
 delete(axesHandlesToChildObjects);
end
axes(handles.ImageSpectrum);
imshow(S,[]);



function LPFreqFilter(handles)
filter_size= str2double(get(handles.size_f,'String'));
D=filter_size;
crntI=getimage(handles.applied_img);
if(size(crntI,3)==3)
    grayImage=rgb2gray(crntI);
else
    grayImage=crntI;
end
A = fft2(double(grayImage)); % compute FFT of the grey image
Y=fftshift(A); % frequency scaling
% defining a typical high pass filter response H(f)
% High pass filter has value=1 in
% the high frequency region and value=0 in the low
% frequency region
[M N]=size(A); % image size
Lo(1:M,1:N)=0;
Lo(abs(0.5*M-D:0.5*M+D),abs(0.5*N-D:0.5*N+D))=1;
K=Y.*Lo;
K1=ifftshift(K);
B2=ifft2(K1);
RenderCurrent(handles,abs(B2));
renderSpectrum(handles);

function HPFreqFilter(handles)
filter_size= str2double(get(handles.size_f,'String'));
D=filter_size;
crntI=getimage(handles.applied_img);
if(size(crntI,3)==3)
    grayImage=rgb2gray(crntI);
else
    grayImage=crntI;
end
A = fft2(double(grayImage)); % compute FFT of the grey image
Y=fftshift(A); % frequency scaling
% defining a typical high pass filter response H(f)
% High pass filter has value=1 in
% the high frequency region and value=0 in the low
% frequency region
[M N]=size(A); % image size
Hi(1:M,1:N)=1;
Hi(abs(0.5*M-D:0.5*M+D),abs(0.5*N-D:0.5*N+D))=0;
K=Y.*Hi;
K1=ifftshift(K);
B2=ifft2(K1);
RenderCurrent(handles,abs(B2));
renderSpectrum(handles);



function size_f_Callback(hObject, eventdata, handles)
% hObject    handle to size_f (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of size_f as text
%        str2double(get(hObject,'String')) returns contents of size_f as a double


% --- Executes during object creation, after setting all properties.
function size_f_CreateFcn(hObject, eventdata, handles)
% hObject    handle to size_f (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in HPFilter.
function HPFilter_Callback(hObject, eventdata, handles)
% hObject    handle to HPFilter (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
HPFreqFilter(handles)

% --- Executes on button press in LPFilter.
function LPFilter_Callback(hObject, eventdata, handles)
% hObject    handle to LPFilter (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
LPFreqFilter(handles)


% --- Executes on button press in HistEq.
function HistEq_Callback(hObject, eventdata, handles)
% hObject    handle to HistEq (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
crntI=getimage(handles.current_img);
crntI=histeq(crntI);
RenderCurrent(handles,crntI);


% --- Executes on button press in HistEq_Ref.
function HistEq_Ref_Callback(hObject, eventdata, handles)
% hObject    handle to HistEq_Ref (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
crntI=getimage(handles.current_img);
[filename,filepath]=uigetfile({'*.*'},'Select Reference Image');
selectedImage = imread(strcat(filepath, filename));
matched = imhistmatch(crntI,selectedImage);
RenderCurrent(handles,matched);


% --- Executes on selection change in SE.
function SE_Callback(hObject, eventdata, handles)
% hObject    handle to SE (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns SE contents as cell array
%        contents{get(hObject,'Value')} returns selected item from SE

switch get(handles.SE,'Value')
    case 1
        textLabel = sprintf('Distance');
        set(handles.MorphoSizeText, 'String', textLabel);  
    case 2
        textLabel = sprintf('Radius');
        set(handles.MorphoSizeText, 'String', textLabel);  
    case 3
        textLabel = sprintf('Pixel Width');
        set(handles.MorphoSizeText, 'String', textLabel);  
    case 4
        textLabel = sprintf('Nonnegative multiple of 3');
        set(handles.MorphoSizeText, 'String', textLabel);          
         
end


% --- Executes during object creation, after setting all properties.
function SE_CreateFcn(hObject, eventdata, handles)
% hObject    handle to SE (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function Morpho_size_Callback(hObject, eventdata, handles)
% hObject    handle to Morpho_size (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Morpho_size as text
%        str2double(get(hObject,'String')) returns contents of Morpho_size as a double


% --- Executes during object creation, after setting all properties.
function Morpho_size_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Morpho_size (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in SE_generate.
function SE_generate_Callback(hObject, eventdata, handles)
% hObject    handle to SE_generate (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
%currentImage2=currentImage;
global SE;
Morpho_size_var1 = str2double(get(handles.Morpho_size,'String'));
switch get(handles.SE,'Value')
    case 1
        
        if (isnan(Morpho_size_var1))
           SE = strel('diamond',5)           
        else
             SE = strel('diamond',Morpho_size_var1)           
        end
    case 2
        if (isnan(Morpho_size_var1))
           SE = strel('disk',5)           
        else
             SE = strel('disk',Morpho_size_var1)           
        end
    case 3
        if (isnan(Morpho_size_var1))
           SE = strel('square',5)           
        else
             SE = strel('square',Morpho_size_var1)           
        end
    case 4
        if (isnan(Morpho_size_var1))
           SE = strel('octagon',3)           
        else
             SE = strel('octagon',Morpho_size_var1)           
        end     
end
%crntI=rgb2gray(SE.Neighborhood);
axesHandlesToChildObjects = findobj(handles.SE_generated, 'Type', 'image');
if ~isempty(axesHandlesToChildObjects)
 delete(axesHandlesToChildObjects);
end
axes(handles.SE_generated)
imshow(SE.Neighborhood);


% --- Executes on selection change in MOBox.
function MOBox_Callback(hObject, eventdata, handles)
% hObject    handle to MOBox (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns MOBox contents as cell array
%        contents{get(hObject,'Value')} returns selected item from MOBox


% --- Executes during object creation, after setting all properties.
function MOBox_CreateFcn(hObject, eventdata, handles)
% hObject    handle to MOBox (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in MO_apply.
function MO_apply_Callback(hObject, eventdata, handles)
% hObject    handle to MO_apply (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global SE;
crntI=getimage(handles.applied_img);
if(size(crntI,3)==3)
    grayImage=rgb2gray(crntI);
else
    grayImage=crntI;
end
%grayImage=imbinarize(crntI,'adaptive');
switch get(handles.MOBox,'Value')
    case 1
         grayImage=imopen(grayImage,SE);      
    case 2
         grayImage=imclose(grayImage,SE);   
    case 3
         grayImage=imerode(grayImage,SE);  
    case 4
         grayImage=imdilate(grayImage,SE);     
    case 5
         grayImage=imfill(grayImage);
    case 6
         grayImage=imtophat(grayImage,SE);  
    case 7
         grayImage=imbothat(grayImage,SE);     
    case 8
         level=graythresh(crntI);
         grayImage=im2bw(crntI,level); % Threshold
         %crntI=getimage(handles.applied_img);
         %grayImage=imbinarize(crntI);
         %grayImage=rgb2gray(grayImage);
         grayImage=bwmorph(grayImage,'skel',Inf);
         %grayImage=bwskel(grayImage);

end

RenderCurrent(handles,grayImage);


% --- Executes on button press in Add_cst_to_img.
function Add_cst_to_img_Callback(hObject, eventdata, handles)
% hObject    handle to Add_cst_to_img (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
Constant = str2double(get(handles.Cst,'String'));
crntI=getimage(handles.current_img);
crntI=imadd(crntI,Constant);
RenderCurrent(handles,crntI);

% --- Executes on button press in Add_img_to_img.
function Add_img_to_img_Callback(hObject, eventdata, handles)
% hObject    handle to Add_img_to_img (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
crntI=getimage(handles.current_img);
[filename,filepath]=uigetfile({'*.*'},'Select Reference Image');
selectedImage = imread(strcat(filepath, filename));
crntI=imadd(crntI,selectedImage);
RenderCurrent(handles,crntI);


function Cst_Callback(hObject, eventdata, handles)
% hObject    handle to Cst (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Cst as text
%        str2double(get(hObject,'String')) returns contents of Cst as a double


% --- Executes during object creation, after setting all properties.
function Cst_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Cst (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in Sub_Img.
function Sub_Img_Callback(hObject, eventdata, handles)
% hObject    handle to Sub_Img (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
crntI=getimage(handles.current_img);
[filename,filepath]=uigetfile({'*.*'},'Select Reference Image');
selectedImage = imread(strcat(filepath, filename));
selectedImage=imcomplement(selectedImage);
crntI=imadd(crntI,selectedImage);
RenderCurrent(handles,crntI);


% --- Executes on button press in Complement.
function Complement_Callback(hObject, eventdata, handles)
% hObject    handle to Complement (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
crntI=getimage(handles.current_img);
crntI=imcomplement(crntI);

RenderCurrent(handles,crntI);



function lowin_Callback(hObject, eventdata, handles)
% hObject    handle to lowin (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of lowin as text
%        str2double(get(hObject,'String')) returns contents of lowin as a double


% --- Executes during object creation, after setting all properties.
function lowin_CreateFcn(hObject, eventdata, handles)
% hObject    handle to lowin (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function highin_Callback(hObject, eventdata, handles)
% hObject    handle to highin (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of highin as text
%        str2double(get(hObject,'String')) returns contents of highin as a double


% --- Executes during object creation, after setting all properties.
function highin_CreateFcn(hObject, eventdata, handles)
% hObject    handle to highin (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function lowout_Callback(hObject, eventdata, handles)
% hObject    handle to lowout (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of lowout as text
%        str2double(get(hObject,'String')) returns contents of lowout as a double


% --- Executes during object creation, after setting all properties.
function lowout_CreateFcn(hObject, eventdata, handles)
% hObject    handle to lowout (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function highout_Callback(hObject, eventdata, handles)
% hObject    handle to highout (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of highout as text
%        str2double(get(hObject,'String')) returns contents of highout as a double


% --- Executes during object creation, after setting all properties.
function highout_CreateFcn(hObject, eventdata, handles)
% hObject    handle to highout (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in Adjust.
function Adjust_Callback(hObject, eventdata, handles)
% hObject    handle to Adjust (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
crntI=getimage(handles.current_img);
if(size(crntI,3)==3)
    grayImage=rgb2gray(crntI);
else
    grayImage=crntI;
end
low_in=str2double(get(handles.lowin,'String'));
high_in=str2double(get(handles.highin,'String'));
low_out=str2double(get(handles.lowout,'String'));
high_out=str2double(get(handles.highout,'String'));
if(~isnan(low_in)&&~isnan(high_in)&&isnan(low_out)&&isnan(high_out))
   grayImage=imadjust(grayImage,[low_in high_in]); 
elseif(~isnan(low_in)&&~isnan(high_in)&&~isnan(low_out)&&~isnan(high_out))
    grayImage=imadjust(grayImage,[low_in high_in],[low_out, high_out]); 
else
    grayImage=imadjust(grayImage);
end

RenderCurrent(handles,grayImage);


% --- Executes on button press in to_gray.
function to_gray_Callback(hObject, eventdata, handles)
% hObject    handle to to_gray (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
crntI=getimage(handles.applied_img);
if(size(crntI,3)==3)
    grayImage=rgb2gray(crntI);
else
    grayImage=crntI;
end
RenderCurrent(handles,grayImage);

% --- Executes on button press in to_binary.
function to_binary_Callback(hObject, eventdata, handles)
% hObject    handle to to_binary (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
crntI=getimage(handles.applied_img);
if(size(crntI,3)==3)
    grayImage=rgb2gray(crntI);
else
    grayImage=crntI;
end
level=graythresh(crntI);
grayImage=im2bw(crntI,level); % Threshold
RenderCurrent(handles,grayImage);