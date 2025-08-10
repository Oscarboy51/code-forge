
import React, { useState } from 'react';

function CaseForm({ onSubmit, onCancel }) {
    const [formData, setFormData] = useState({
        diagnosis: '',
        patientId: '',
        procedure: '',
        complications: '',
        images: null
    });

    const handleChange = (e) => {
        const { name, value, files } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: files ? files[0] : value
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        const newCase = {
            id: `C-${String(Date.now()).slice(-4)}`,
            ...formData,
            status: 'Pre-Op',
            createdAt: new Date().toISOString()
        };
        onSubmit(newCase);
    }

    return (
        <div className="form-container">
            <form onSubmit={handleSubmit}>
                <h2>New Surgical Case</h2>

                <fieldset>
                    <legend>Pre-Operative</legend>
                    <label>
                        Diagnosis:
                        <input
                            type="text"
                            name="diagnosis"
                            value={formData.diagnosis}
                            onChange={handleChange}
                            required
                        />
                    </label>
                    <label>
                        Patient ID:
                        <input
                            type="text"
                            name="patientId"
                            value={formData.patientId}
                            onChange={handleChange}
                            required
                        />
                    </label>
                </fieldset>

                <fieldset>
                    <legend>Intra-Operative</legend>
                    <label>
                        Procedure:
                        <input
                            type="text"
                            name="procedure"
                            value={formData.procedure}
                            onChange={handleChange}
                            required
                        />
                    </label>
                    <label>
                        Upload Images:
                        <input
                            type="file"
                            name="images"
                            accept="image/,video/"
                            onChange={handleChange}
                        />
                    </label>
                </fieldset>

                <fieldset>
                    <legend>Post-Operative</legend>
                    <label>
                        Complications:
                        <textarea
                            name="complications"
                            value={formData.complications}
                            onChange={handleChange}
                        />
                    </label>
                </fieldset>

                <div className="form-actions">
                    <button type="submit">Save Case</button>
                    <button type="button" onClick={onCancel}>Cancel</button>
                </div>
            </form>
        </div>
    );

}
export default CaseForm;
